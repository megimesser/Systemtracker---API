from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional
from random import randint

app = FastAPI()

@app.get("/") #-- Method mit Path
async def root():  #-- Funktion
    return {"Test"}

# pip install fastapi --all  - installiert mit uvicorn

# Start uvicorn main:app - läuft über Port 8000
# Der Status wird immer von oben nach unten durchgerendert - 
# Die erste Pathoperation wird immer als erstes genommen 


#post 
@app.post("/test_post")
# Muss in Postman über den Body eingefügt werden
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"message": payload}


# Datenvalidierung über pydantic
# Pydanticmodel
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None




# Der Inhalt von Post wird hier validiert
@app.post("/createposts")
def create_posts(new_post: Post): # new_post ist hier die Erweiterung vom BaseModel
    print(new_post) # Pydantic Model
    print(new_post.model_dump()) # Python Dictionary
    return {"message": new_post}


my_posts = [{"title":"test", "id":3}
]




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
def get_posts(id: int):
    for post in my_posts:
        if post["id"] == id:
            return post
    
    return {"message": "Post not found"}