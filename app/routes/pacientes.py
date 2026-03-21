from fastapi import APIRouter, HTTPException
from app.models import Paciente

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])

# db temporal
db_pacientes = []


@router.post("/ingreso")
async def crear_paciente(paciente: Paciente):
    # aqui Pydantic ya valido todo

    for p in db_pacientes:
        if p.email == paciente.email:
            raise HTTPException(
                status_code=400, detail="El paciente ya esta registrado."
            )

    db_pacientes.append(paciente)
    return {"status": "success", "msg": "Pacientes registrado", "data": paciente}


@router.get("/")
async def gets_pacientes():
    return db_pacientes
