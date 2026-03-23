from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.routes import pacientes

"""origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://redautoshop.com.ar",
    "https://www.redautoshop.com.ar",
] """

app = FastAPI(title=settings.APP_NAME)

# cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
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
        "app_name": settings.APP_NAME,
        "debug_mode": settings.DEBUG,
    }
