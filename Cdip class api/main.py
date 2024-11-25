import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI

import requests


app = FastAPI()

class Multi(BaseModel):
    strin : str


@app.get("/")
def read_root():
    return {"HI": "World"}

@app.get("/name")
def read_name():
    return {"name": "Mashrafe"}


@app.post("/multiply")
def multiply(mul: Multi):
    return {"result": mul.num * 10}


@app.post("/fincode")
def multiply(mul: Multi):
    url = f"https://www.finn.no/{mul.strin}"
    response = requests.get(url)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")
    section = soup.find("section")

    heading = section.find("h1").text
    return {"result": heading}

if __name__ == "__main__":
    uvicorn.run(app)