"""API de productos con FastAPI.

Incluye:
- Listado paginado por 3 elementos
- Filtro por nombre
- CRUD completo
"""

from __future__ import annotations  # Permite anotaciones pospuestas para tipos.

from typing import List, Optional  # Tipos auxiliares para respuestas y parámetros.

from fastapi import Depends, FastAPI, HTTPException, Query, status  # Componentes clave de FastAPI.
from sqlalchemy.orm import Session  # Tipo de sesión de SQLAlchemy.

from app import crud  # Funciones CRUD para la base de datos.
from app.db import get_db, init_db  # Dependencia de DB e inicialización.
from app.schemas import ProductCreate, ProductRead, ProductUpdate  # Esquemas de entrada/salida.

app = FastAPI(title="API de Productos - Story")  # Instancia principal de la API.


@app.on_event("startup")  # Hook que se ejecuta al iniciar la app.
def on_startup() -> None:  # Función de arranque sin retorno.
    """Inicializa la base de datos al arrancar la app."""

    init_db()  # Crea tablas e inserta datos iniciales si hace falta.


@app.get("/products", response_model=List[ProductRead])  # Endpoint de listado.
def list_products(  # Handler para listar productos.
    skip: int = Query(0, ge=0, description="Offset de paginación"),  # Desde qué fila iniciar.
    limit: int = Query(3, ge=1, le=100, description="Tamaño de página"),  # Máximo de filas.
    name: Optional[str] = Query(None, min_length=1, description="Filtro por nombre"),  # Filtro opcional.
    db: Session = Depends(get_db),  # Sesión de BD inyectada.
):
    """Lista productos con paginación y filtro opcional."""

    return crud.get_products(db=db, skip=skip, limit=limit, name=name)  # Ejecuta consulta paginada.


@app.get("/products/{product_id}", response_model=ProductRead)  # Endpoint por ID.
def get_product(product_id: int, db: Session = Depends(get_db)):  # Handler de detalle.
    """Obtiene un producto por ID."""

    product = crud.get_product(db, product_id)  # Busca el producto en BD.
    if not product:  # Verifica si existe.
        raise HTTPException(status_code=404, detail="Producto no encontrado")  # Error 404 si no está.
    return product  # Devuelve el producto encontrado.


@app.post("/products", response_model=ProductRead, status_code=status.HTTP_201_CREATED)  # Endpoint de creación.
def create_product(payload: ProductCreate, db: Session = Depends(get_db)):  # Handler de creación.
    """Crea un nuevo producto."""

    return crud.create_product(db, payload)  # Inserta en la base de datos.


@app.put("/products/{product_id}", response_model=ProductRead)  # Endpoint de edición.
def update_product(  # Handler de actualización.
    product_id: int,  # ID del producto a editar.
    payload: ProductUpdate,  # Datos a actualizar.
    db: Session = Depends(get_db),  # Sesión de BD.
):
    """Edita un producto existente."""

    product = crud.get_product(db, product_id)  # Busca el producto actual.
    if not product:  # Si no existe.
        raise HTTPException(status_code=404, detail="Producto no encontrado")  # Responde 404.
    return crud.update_product(db, product, payload)  # Aplica cambios.


@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)  # Endpoint de borrado.
def delete_product(product_id: int, db: Session = Depends(get_db)):  # Handler de eliminación.
    """Elimina un producto."""

    product = crud.get_product(db, product_id)  # Busca el producto.
    if not product:  # Si no existe.
        raise HTTPException(status_code=404, detail="Producto no encontrado")  # Responde 404.
    crud.delete_product(db, product)  # Elimina de la BD.
    return None  # Respuesta vacía para 204.
