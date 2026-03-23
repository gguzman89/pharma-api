import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

env_actual = os.getenv("ENV", "development")
env_file = f".env.{env_actual}"

if os.path.exists(env_file):
    load_dotenv(env_file, override=True)


class Settings(BaseSettings):
    APP_NAME: str = os.getenv("APP_NAME", "Pharma API")
    ENV: str = env_actual
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", 8000))
    DEBUG: bool = os.getenv("DEBUG") == "True"

    _origins: str = os.getenv("ALLOWED_ORIGINS", "")

    @property
    def ALLOWED_ORIGINS(self) -> list[str]:
        return [o.strip() for o in self._origins.split(",")] if self._origins else ["*"]


# singleton
settings = Settings()
