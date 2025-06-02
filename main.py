from fastapi import FastAPI, Request
from .connexio import conn
from .Servei import user

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/register")
async def register_user(nom : str, cognom: str, email: str, descripcio: str, curs: str, any: int, dirrecio: str, codi_postal: str, password: str):
    return user.register_user()


