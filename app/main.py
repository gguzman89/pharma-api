import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.models import Paciente

load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "Pharma API"))


@app.get("/")
def read_root():
    return {"hola": "Mendoza", "chip": "M4"}


@app.get("/config")
def get_config():
    return {
        "app_name": os.getenv("APP_NAME"),
        "debug_mode": os.getenv("DEBUG") == "True",
    }


@app.post("/pacientes/ingreso")
async def crear_paciente(paciente: Paciente):
    # aqui Pydantic ya valido todo
    return {"status": "success", "data": paciente}
