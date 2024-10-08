from fastapi import FastAPI
from pydantic import BaseModel
from super_db import usuarios, items
app = FastAPI()

@app.get("/")
def get_base():
    return {"Otra": "cosa"}

@app.get("/usuario/{id}")
def get_usuario(id:int):
    usuario = usuarios.get(id)
    if not usuario:
        return "No se encontró el usuario."
    return usuario


@app.put("/usuario/favorito")
def put_favorito(nombre: str, ultima_fecha: str, id: int):
    usuario = usuarios.get(id)
    if not usuario:
        return "No se encontró el usuario."
    usuario['favoritos'].append({
        "nombre": nombre, "ultima-fecha": ultima_fecha,
    })
    return usuario

@app.get("/item")
def getItem(id: str):
    item = items.get(id)
    if not item:
        return "No se encontró el usuario."
    return item

class Usuario(BaseModel):
    nombre:str
    apellido:str
    edad: int
    favoritos: list[str] | None = None


@app.post("/usuario")
def post_usuario(usuario: Usuario):
    ultimo_id = len(usuarios)
    usuarios[ultimo_id + 1] = usuario.model_dump()
    print(usuarios)
    return "Guardado" 