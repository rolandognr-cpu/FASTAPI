from typing import Union

from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Hello World!!"}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return payload
    #return {"message": "succesfully created posts"}

#----------------------------------------------------------------------------------------



