# ORM = Layer of Abstraction zwischen der Datenbank und uns
import json
import os
import time

import psycopg2
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
from sqlalchemy.orm import Session

from config import COUNTER_DATA, DATABASE_DB, DATABASE_PW, DATABASE_USER
from Datenbank.db import get_db
from Datenbank.models import Datentraeger

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


def opener(pfad):
    with open(pfad, encoding="utf-8") as f:
        return json.load(f)


# ---------- Datenbank (psycopg2) ----------

def get_connection(max_versuche: int = 5):
    """Öffnet eine NEUE Verbindung pro Request."""
    for versuch in range(1, max_versuche + 1):
        try:
            return psycopg2.connect(
                host="localhost",
                port=5433,
                dbname=DATABASE_DB,
                user=DATABASE_USER,
                password=DATABASE_PW,
                cursor_factory=RealDictCursor,
            )
        except psycopg2.OperationalError as error:
            print(f"Verbindung fehlgeschlagen (Versuch {versuch}/{max_versuche}): {error}")
            time.sleep(2)
    raise HTTPException(status_code=503, detail="Datenbank nicht erreichbar")


def hole(cursor, tabelle: str, hostname: str, limit: int) -> list[dict]:
    """Holt die neuesten Zeilen einer Tabelle für genau einen Host."""
    cursor.execute(
        sql.SQL("SELECT * FROM {} WHERE hostname = %s ORDER BY id DESC LIMIT %s")
        .format(sql.Identifier(tabelle)),
        (hostname, limit),
    )
    return cursor.fetchall()


def alle_hosts(cursor) -> list[str]:
    """Holt alle Hostnamen, die jemals Daten geschrieben haben."""
    cursor.execute("SELECT DISTINCT hostname FROM hostinformation ORDER BY hostname")
    return [row["hostname"] for row in cursor.fetchall()]


# ---------- Dashboard ----------

@app.get("/dashboard")
def dashboard_start():
    conn = get_connection()
    try:
        with conn, conn.cursor() as cursor:
            hosts = alle_hosts(cursor)
    finally:
        conn.close()

    if not hosts:
        raise HTTPException(status_code=404, detail="Noch keine Hosts mit Daten")
    return RedirectResponse(url=f"/dashboard/{hosts[0]}")


@app.get("/dashboard/{hostname}", response_class=HTMLResponse)
def dashboard(request: Request, hostname: str):
    limits = opener(COUNTER_DATA)

    conn = get_connection()
    try:
        with conn, conn.cursor() as cursor:
            hosts = alle_hosts(cursor)
            if hostname not in hosts:
                raise HTTPException(status_code=404, detail=f"Host {hostname} unbekannt")

            context = {
                "hosts": hosts,
                "current": hostname,
                "host":    hole(cursor, "hostinformation", hostname, limits["HOST"]),
                "sys":     hole(cursor, "sysinformation", hostname, limits["SYS"]),
                "temp":    hole(cursor, "temperaturinformation", hostname, limits["TEMP"]),
                "docker":  hole(cursor, "dockerinformation", hostname, limits["DOCKER"]),
                "prozess": hole(cursor, "prozessinformation", hostname, 10),
                "ram":     hole(cursor, "raminformation", hostname, limits["RAM"]),
                "disc":    hole(cursor, "discinformation", hostname, limits["DATA"]),
            }
    finally:
        conn.close()

    return templates.TemplateResponse(request, "index.html", context)


# ---------- ORM-Routen ----------

class Testmodel(BaseModel):
    test: str


# Alle Einträge per ORM
@app.get("/get/orm")
def get_all_orm(db: Session = Depends(get_db)):
    posts = db.query(Datentraeger).all()
    return {"status": posts}


# Neuer Eintrag per ORM
@app.post("/post/orm", status_code=status.HTTP_201_CREATED)
def create_post_orm(testmodel: Testmodel, db: Session = Depends(get_db)):
    new_post = Datentraeger(
        hostname="test",
        available=testmodel.test,
        filesystem=testmodel.test,
        size=testmodel.test,
        mounted_on=testmodel.test,
        used=testmodel.test,
        capacity=testmodel.test,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}


# Eintrag per ID / ORM
@app.get("/get_post/orm/{id}")
def get_post_orm(id: int, db: Session = Depends(get_db)):
    post = db.query(Datentraeger).filter(Datentraeger.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {"status": post}


# Löschen per ID / ORM
@app.delete("/get_post/orm/{id}")
def delete_post_orm(id: int, db: Session = Depends(get_db)):
    post = db.query(Datentraeger).filter(Datentraeger.id == id)
    if post.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    post.delete(synchronize_session=False)
    db.commit()
    return {"deleted": id}


# Update per ID / ORM
@app.put("/put_posts/orm/{id}")
def update_post_orm(id: int, db: Session = Depends(get_db)):
    post_query = db.query(Datentraeger).filter(Datentraeger.id == id)
    if post_query.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    post_query.update({"filesystem": "Dies ist ein Update"}, synchronize_session=False)
    db.commit()
    return {"updated": id}