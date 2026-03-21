import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes import pacientes

load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "Pharma API"))

# routes
app.include_router(pacientes.router)


@app.get("/")
def read_root():
    return {"hola": "Mendoza", "chip": "M4"}


@app.get("/config")
def get_config():
    return {
        "app_name": os.getenv("APP_NAME"),
        "debug_mode": os.getenv("DEBUG") == "True",
    }
