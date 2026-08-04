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

# import des jinja2 Frameworks 
import os
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

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





