#ORM 
# ORM = Layer of Abstraction zwischen der Datenbank und uns 
from fastapi import FastAPI, Body, Response, status, Request, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randint
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from config import DATABASE_DB, DATABASE_PW, DATABASE_USER
from Datenbank.db import get_session, get_db
from Datenbank.models import Datentraeger


from sqlalchemy.orm import Session, sessionmaker,query
# import des jinja2 Frameworks 
import os
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Depends, FastAPI, HTTPException, Body

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

while True:
    try: 
        conn = psycopg2.connect(host = "localhost",port= 5433,database = DATABASE_DB, user = DATABASE_USER, password = DATABASE_PW,cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error: 
        print("Connection to Database failed ")
        print("ERROR :", error)
        time.sleep(2)


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    cursor.execute("""SELECT * FROM discinformation""")
    posts = cursor.fetchall()
    return templates.TemplateResponse(
    request,                                    # request als ERSTES Argument
    "index.html",                               # dann der Template-Name
    {"titel": posts}                  # dann der Context (ohne request!)
)




# Get all per ORM 
@app.get("/get/orm")
def create_hero(db: Session = Depends(get_db)):
    posts = db.query(Datentraeger).all()
    return{"status": posts}


class Testmodel(BaseModel):
    test: str

# neur Eintrag per ORM 
@app.post("/post/orm", status_code=status.HTTP_201_CREATED)
def create_posts(testmodel: Testmodel, db: Session = Depends(get_db)):


# Mit einfacherrer Schreibweise 
# ** entpackt das dictionary
    #print(**post.dict())

#    new_post = Datenträger(
#        **post.dict()
#    )

    new_post = Datentraeger(
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



# get post by id / ORM
@app.get("/get_post/orm/{id}")
def get_post(id: int, db: Session = Depends(get_db)):

    post = db.query(Datentraeger).filter(Datentraeger.id == id).first()

    

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} was not found")
    
    return {"status": post}




# delete by id / ORM 
@app.delete("/get_post/orm/{id}")
def get_post(id: int, db: Session = Depends(get_db)):

    post = db.query(Datentraeger).filter(Datentraeger.id == id)

    if post.first() == None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} was not found")
    
    post.delete(synchronize_session=False)
    db.commit()




# Put über ORM 
@app.put("/put_posts/orm/{id}")
def get_post(id: int, db: Session = Depends(get_db)):

    post_query = db.query(Datentraeger).filter(Datentraeger.id == id )

    post_catch = post_query.first()

    if post_catch  == None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id: {id} was not found")
    


    post_query.update({'filesystem':"Dies ist ein Update"}, synchronize_session=False)

#Hier kann auch das pydanticmodel eingefügt werden 
#        post_query.update({Testmodel.dict()}, synchronize_session=False)
#        Dafür mus innerhalb der Funktion noch "testmodel: Testmodel" hinzugefügt werden
    db.commit()

    return "past"
    

