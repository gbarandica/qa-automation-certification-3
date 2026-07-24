"""Reto de la Sesión 4: CRUD de usuarios con HTTPX y pytest.

Esta suite refactoriza a Python la colección de Postman creada en la Sesión 3.
Todos los requests utilizan la fixture compartida `api`.
"""
import json
import time
from pathlib import Path

import pytest
import time


CONTRATO_USER = {
    "id": int,
    "name": str,
    "username": str,
    "email": str,
}

RUTA_DATOS = Path(__file__).parent.parent / "data" / "users_payloads.json"

with RUTA_DATOS.open(encoding="utf-8") as archivo:
    USERS_PAYLOADS = json.load(archivo)


def cumple_contrato(recurso: dict, contrato: dict) -> bool:
    """Valida que los campos existan y tengan el tipo esperado."""
    return all(
        campo in recurso and isinstance(recurso[campo], tipo)
        for campo, tipo in contrato.items()
    )

def test_listar_users(api):
    respuesta = api.get("/users")

    assert respuesta.status_code == 200
    assert len(respuesta.json()) == 10

def test_detalle_cumple_contrato(api):
    respuesta = api.get("/users/1")
    usuario = respuesta.json()

    assert respuesta.status_code == 200
    assert cumple_contrato(usuario, CONTRATO_USER)

def test_crear_user(api):
    nombre_unico = f"Usuario QA {time.time_ns()}"
    payload = {
        "name": nombre_unico,
        "username": "qa_automation",
        "email": "qa_automation@example.com"
    }
    respuesta = api.post("/users", json=payload)

    assert respuesta.status_code == 201
    assert cumple_contrato(respuesta.json(), CONTRATO_USER)

def test_actualizar_user(api):
    nombre_actualizado = f"Usuario Actualizado {time.time_ns()}"

    payload = {
        "id": 1,
        "name": nombre_actualizado,
        "username": "qa_updated",
        "email": "qa.updated@example.com",
    }

    respuesta = api.put("/users/1", json=payload)
    usuario_actualizado = respuesta.json()

    assert respuesta.status_code == 200
    assert usuario_actualizado["name"] == nombre_actualizado

def test_eliminar_user(api):
    respuesta = api.delete("/users/1")

    assert respuesta.status_code == 200
    assert respuesta.json() == {}

@pytest.mark.parametrize("payload_base", USERS_PAYLOADS)
def test_crear_users_con_datos_externos(api, payload_base):
    payload = payload_base.copy()
    payload["name"] = f'{payload["name"]} {time.time_ns()}'

    respuesta = api.post("/users", json=payload)
    usuario_creado = respuesta.json()

    assert respuesta.status_code == 201
    assert usuario_creado["name"] == payload["name"]
    assert usuario_creado["username"] == payload["username"]
    assert usuario_creado["email"] == payload["email"]
