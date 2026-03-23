import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

env_actual = os.getenv("ENV", "development")
env_file = f".env.{env_actual}"

if os.path.exists(env_file):
    load_dotenv(env_file, override=True)
    print(f"Cargado env: {env_file}")
else:
    print(f"No se encontro {env_file}, usando valores por default")

if __name__ == "__main__":
    print(f"--- Arrancando en modo: {env_actual.upper()} ---")

    uvicorn.run(
        "app.main:app",
        host=os.getenv("HOST", "127.0.0.1"),
        port=int(os.getenv("PORT", 8000)),
        reload=(env_actual == "development"),
    )
