from pydantic import BaseModel, Field, EmailStr
from typing import Optional


# define schema data user
class Paciente(BaseModel):
    nombre: str = Field(..., min_length=2, json_schema_extra={"example": "Gabriel"})
    edad: int = Field(..., gt=0, lt=120)
    email: EmailStr
    sintomas: Optional[str] = None
