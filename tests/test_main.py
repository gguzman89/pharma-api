from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["chip"] == "M4"


def test_crear_paciente_valido():
    payload = {"nombre": "Gabriel", "edad": 36, "email": "gabriel@uncuyo.edu.ar"}
    response = client.post("/pacientes/ingreso", json=payload)
    assert response.status_code == 200
    assert response.json()["data"]["nombre"] == "Gabriel"
