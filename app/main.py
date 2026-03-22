import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from app.routes import pacientes

load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "Pharma API"))

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
