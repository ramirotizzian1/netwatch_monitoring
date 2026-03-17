from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
import os

app = FastAPI(title="Net-Watch API", description="API Gateway con Inventario de Nodos")

# Conexión a MongoDB (Lee la URI desde las variables de entorno de Render)
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017") # Fallback local
client = MongoClient(MONGO_URI)
db = client["netwatch_db"]
collection = db["nodos"]

# Modelo de datos para validación
class NodoRed(BaseModel):
    ip: str
    hostname: str
    fabricante: str  # Ej: "Cisco", "MikroTik", "Linux"
    estado: str = "activo"

@app.get("/health")
def health_check():
    return {"status": "ok", "database": "conectada" if client.admin.command('ping') else "error"}

@app.post("/api/v1/nodos", status_code=201)
def agregar_nodo(nodo: NodoRed):
    """Guarda un nuevo equipo en la base de datos"""
    nodo_dict = nodo.dict()
    resultado = collection.insert_one(nodo_dict)
    return {"mensaje": "Nodo agregado con éxito", "id": str(resultado.inserted_id)}

@app.get("/api/v1/nodos")
def listar_nodos():
    """Recupera todos los equipos del inventario"""
    nodos = []
    for doc in collection.find({}, {"_id": 0}): # Excluimos el Object_ID interno para simplificar
        nodos.append(doc)
    return {"total": len(nodos), "inventario": nodos}