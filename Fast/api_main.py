from fastapi import FastAPI, Body

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