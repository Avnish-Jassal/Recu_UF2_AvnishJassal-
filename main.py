from fastapi import FastAPI, Request
from Servei.user import get_user
from connexio import conn
from Servei import user
from Servei.user import delete_user

app = FastAPI()

@app.post("/register")
async def register_user(nom : str, cognom: str, email: str, descripcio: str, curs: str, any: int, dirrecio: str, codi_postal: str, password: str):
    return user.register_user()

@app.get("/perfil/{user_id}")
async def perfil(user_id: int):
    return user.get_user(user_id)

@app.put("/perfil{user_id}")
async def update_perfil(user_id : int, cognom : str, dirrecio : str):
    return user.update_perfil(user_id, cognom, dirrecio)

@app.delete("/perfil/{id}")
async def delete_user(user_id : int):
    return user.delete_user(user_id)