import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
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


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Ocurrio algo inesperado", "detail": str(exc)},
    )


@app.get("/")
def read_root():
    return {"hola": "Mendoza", "chip": "M4"}


@app.get("/config")
def get_config():
    return {
        "app_name": os.getenv("APP_NAME"),
        "debug_mode": os.getenv("DEBUG") == "True",
    }
