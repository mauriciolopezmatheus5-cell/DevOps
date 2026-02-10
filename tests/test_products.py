"""Pruebas de la API de productos."""

from __future__ import annotations  # Anotaciones pospuestas.

import importlib  # Recarga de módulos.
import os  # Variables de entorno.
from pathlib import Path  # Manejo de rutas.

import pytest  # Framework de pruebas.
from fastapi.testclient import TestClient  # Cliente de pruebas HTTP.


@pytest.fixture()  # Fixture reutilizable.
def client(tmp_path):  # Cliente configurado con BD temporal o externa.
    """Cliente de pruebas con base de datos temporal."""

    existing_url = os.getenv("DATABASE_URL")  # Lee URL existente.
    if not existing_url:  # Si no hay URL externa.
        db_path = tmp_path / "test_story.db"  # Ruta de BD temporal.
        os.environ["DATABASE_URL"] = f"sqlite:///{db_path}"  # Configura URL de BD.

    # Importación tardía para usar DATABASE_URL del entorno
    from app import main as main_module  # Importa la app con la URL actual.

    importlib.reload(main_module)  # Recarga para aplicar el entorno.

    with TestClient(main_module.app) as test_client:  # Crea cliente HTTP.
        yield test_client  # Entrega el cliente al test.


def test_list_products_default_pagination(client):  # Prueba paginación por defecto.
    """La lista debe devolver 3 productos por defecto."""

    response = client.get("/products")  # Llama al listado.
    assert response.status_code == 200  # Debe ser OK.
    data = response.json()  # Obtiene JSON.
    assert isinstance(data, list)  # Debe ser lista.
    assert len(data) == 3  # Tamaño por defecto.


def test_list_products_filter_by_name(client):  # Prueba filtro por nombre.
    """Filtro por nombre debe devolver coincidencias."""

    response = client.get("/products", params={"name": "Paracetamol"})  # Llama con filtro.
    assert response.status_code == 200  # Debe ser OK.
    data = response.json()  # Obtiene JSON.
    assert len(data) >= 1  # Debe encontrar resultados.
    assert "Paracetamol" in data[0]["name"]  # Verifica coincidencia.


def test_crud_product(client):  # Prueba CRUD completo.
    """Crear, editar y eliminar un producto."""

    payload = {  # Datos para crear.
        "name": "Ketorolaco 10mg",  # Nombre.
        "description": "Analgésico",  # Descripción.
        "price": 5.25,  # Precio.
        "stock": 33,  # Stock.
    }
    create_resp = client.post("/products", json=payload)  # Crea producto.
    assert create_resp.status_code == 201  # Debe crear.
    created = create_resp.json()  # Lee respuesta.
    product_id = created["id"]  # Guarda ID.

    update_resp = client.put(  # Actualiza producto.
        f"/products/{product_id}",  # Endpoint con ID.
        json={"price": 6.00, "stock": 40},  # Nuevos valores.
    )
    assert update_resp.status_code == 200  # Debe ser OK.
    updated = update_resp.json()  # Lee respuesta.
    assert updated["price"] == 6.00  # Verifica precio.
    assert updated["stock"] == 40  # Verifica stock.

    delete_resp = client.delete(f"/products/{product_id}")  # Elimina producto.
    assert delete_resp.status_code == 204  # Debe borrar.

    get_resp = client.get(f"/products/{product_id}")  # Consulta eliminado.
    assert get_resp.status_code == 404  # Debe no existir.
