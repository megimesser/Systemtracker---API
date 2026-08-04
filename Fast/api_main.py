from fastapi import FastAPI, Body, Response, status, Request, HTTPException
from pydantic import BaseModel
from typing import Optional
from random import randint
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from config import DATABASE_PW

# import des jinja2 Frameworks 
import os
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

print(DATABASE_PW)




@app.get("/") #-- Method mit Path
async def root():  #-- Funktion
    return {"Test"}

# pip install fastapi --all  - installiert mit uvicorn

# Start uvicorn main:app - läuft über Port 8000
# Der Status wird immer von oben nach unten durchgerendert - 
# Die erste Pathoperation wird immer als erstes genommen 



# Datenvalidierung über pydantic
# Pydanticmodel
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

while True:
    try: 
        conn = psycopg2.connect(host =  "localhost",database = "postgres", user = "postgres", password = DATABASE_PW,cursor_factory = RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was succesfull!")
        break
    except Exception as error: 
        print("Connection to Database failed ")
        print("ERROR :", error)
        time.sleep(2)

        


### Abruf von Datenbank via Pyhton
#Post retrieven übe Python 
@app.get("/python/posts")
def get_pposts():
    cursor.execute("""SELECT * FROM public.testtable""")
    posts = cursor.fetchall()
    print(posts)
    return{"data": posts}


#create posts
@app.post("/python/post", status_code=status.HTTP_201_CREATED)
def create_posts(payload: Post):

    cursor.execute(
        """
        INSERT INTO public.testtable (name, number)
        VALUES (%s, %s) RETURNING *
        """,
        (payload.title, payload.number)
    )

    #back = cursor.fetchone()

    conn.commit()

    return payload, 


# Post per ID Fetchen 
@app.get("/python/posts/{id}")
def fetch_posts(id: int):

    cursor.execute(
        """SELECT * FROM public.testtable WHERE id = %s""",
        (id,)
    )
    post = cursor.fetchone()
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id:{id} was not found"
        )

    return post



# Deleting per ID python 
@app.delete("/python/posts/{id}")
def delete_posts(id: int):

    cursor.execute(
        """DELETE  FROM public.testtable WHERE id = %s RETURNING *""",(id,)
    )
    delete_post = cursor.fetchall()
    conn.commit()

    if not delete_post: 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id:{id} was not found"
        )

    
#Updating per ID Pyton

@app.put("/python/posts/{id}")
def update_posts(id: int, payload: dict = Body(...)):

    cursor.execute(
        """
        UPDATE public.testtable
        SET name = %s, number = %s
        WHERE id = %s
        RETURNING *
        """,
        (payload["name"], payload["number"], id)
    )

    update_post = cursor.fetchone()
    conn.commit()

    if not update_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id:{id} was not found"
        )

    return update_post


### Dashboard

@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    cursor.execute("""SELECT * FROM public.testtable""")
    posts = cursor.fetchall()
    return templates.TemplateResponse(
    request,                                    # request als ERSTES Argument
    "index.html",                               # dann der Template-Name
    {"titel": posts}                  # dann der Context (ohne request!)
)















# Testdictionary
my_posts = [{"title":"test", "id":3}
]





#post 
@app.post("/test_post")
# Muss in Postman über den Body eingefügt werden
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"message": payload}





# Der Inhalt von Post wird hier validiert
@app.post("/createposts")
def create_posts(new_post: Post): # new_post ist hier die Erweiterung vom BaseModel
    print(new_post) # Pydantic Model
    print(new_post.model_dump()) # Python Dictionary
    my_posts.append(new_post.model_dump())
    return {"message": new_post}






@app.post("/addmyposts")
def addmyposts(new_post: dict = Body(...)):
    print(new_post)

    randomint = randint(0, 1000)
    randomint = int(randomint)

    my_posts.append({
        "title": new_post["title"],
        "id": randomint
    })

    print(my_posts)


    return my_posts


# mit Einsatz des Schemas 
@app.post("/posts_send")
def create_posts(post: Post):
    post_dict = post.model_dump()
    post_dict["id"] = randint(0, 1000)
    my_posts.append(post_dict)

    return post_dict

# Gesendeter Body über Postman 
"""{
    "title": "test_5"
}"""


#Die id muss hier als Integer mitgegeben werden ansonßten bekommt man einen Type Error 
# Post retrieven # Id ist hier der Pathparameter
@app.get("/posts/{id}")
def get_posts(id: int, response: Response):
    for post in my_posts:
        if post["id"] == id:
            return post
        
    """
        Responsecode für bestimmten Statuscode 
        elif not post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
            response.status_code =  status...
            return {"message": f"post with id: {id} was not found"}


    """
    
    return {"message": "Post not found"}


@app.delete("/deletepost/{id}", status_code=status.HTTP_204_NO_CONTENT)
def deletepost(id: int):
    """
    for i, p enumerate(my_posts):
        if p["id"] == id:
    """
        
    for post in my_posts:
        if post["id"] == id:
            my_posts.pop(post)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        return("post - ID ist nicht vorhanden")
    

@app.get("/showpost")
def showposts():
    return my_posts

#path parameter können pro request method 1x den gleichen Namen tragen 
@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail" : post}



def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i
    return None



@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)

    post_dict = post.model_dump()
    post_dict["id"]

    my_posts[index] = post_dict



    return { "message": "updated post"}
