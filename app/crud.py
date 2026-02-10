"""Funciones CRUD para productos."""

from __future__ import annotations  # Anotaciones pospuestas.

from typing import List, Optional  # Tipos auxiliares.

from sqlalchemy.orm import Session  # Sesión de BD.

from app.models import Product  # Modelo ORM.
from app.schemas import ProductCreate, ProductUpdate  # Esquemas de entrada.


def get_product(db: Session, product_id: int) -> Optional[Product]:  # Obtener por ID.
    """Obtiene un producto por ID."""

    return db.query(Product).filter(Product.id == product_id).first()  # Consulta y retorna el primero.


def get_products(  # Listar productos.
    db: Session,  # Sesión de BD.
    skip: int = 0,  # Offset.
    limit: int = 3,  # Límite.
    name: Optional[str] = None,  # Filtro opcional.
) -> List[Product]:
    """Lista productos con paginación y filtro por nombre."""

    query = db.query(Product)  # Consulta base.
    if name:  # Si hay filtro.
        # Búsqueda parcial por nombre (case-insensitive en SQLite)
        query = query.filter(Product.name.ilike(f"%{name}%"))  # Aplica filtro.
    return query.order_by(Product.id).offset(skip).limit(limit).all()  # Pagina y retorna.


def create_product(db: Session, payload: ProductCreate) -> Product:  # Crear producto.
    """Crea un nuevo producto."""

    product = Product(**payload.model_dump())  # Construye el modelo.
    db.add(product)  # Agrega a la sesión.
    db.commit()  # Guarda en BD.
    db.refresh(product)  # Recarga datos (ID, etc.).
    return product  # Devuelve el creado.


def update_product(db: Session, product: Product, payload: ProductUpdate) -> Product:  # Actualizar producto.
    """Actualiza un producto existente."""

    data = payload.model_dump(exclude_unset=True)  # Solo campos enviados.
    for key, value in data.items():  # Recorre cada campo.
        setattr(product, key, value)  # Actualiza el atributo.
    db.commit()  # Guarda cambios.
    db.refresh(product)  # Recarga desde BD.
    return product  # Devuelve actualizado.


def delete_product(db: Session, product: Product) -> None:  # Eliminar producto.
    """Elimina un producto."""

    db.delete(product)  # Marca para eliminar.
    db.commit()  # Ejecuta borrado.
