from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/") #-- Method mit Path
async def root():  #-- Funktion
    return {"Test"}

# pip install fastapi --all  - installiert mit uvicorn

# Start uvicorn main:app - läuft über Port 8000
# Der Status wird immer von oben nach unten durchgerendert - 
# Die erste Pathoperation wird immer als erstes genommen 


#post 
@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"message": payload}


# Datenvalidierung über pydantic

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title":"test", "id":3}
]

# Der Inhalt von Post wird hier validiert
@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post) # Pydantic Model
    print(new_post.dict()) # Python Dictionary
    return {"message": new_post}


# Post retrieven # Id ist hier der Pathparameter
@app.get("/posts/{id}")
#Die id muss hier als Integer mitgegeben werden ansonßten bekommt man einen Type Error 
def get_posts(id: int):
    for post in my_posts:
        if post["id"] == id:
            return post
    
    return {"message": "Post not found"}