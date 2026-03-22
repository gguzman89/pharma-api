import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.routes import pacientes

load_dotenv()

"""origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://redautoshop.com.ar",
    "https://www.redautoshop.com.ar",
] """

app = FastAPI(title=os.getenv("APP_NAME", "Pharma API"))

# cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS").split(","),
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH"],
    allow_headers=["Content-Type", "Authorization"],
)

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
