"""Modelos ORM para la base de datos."""

from __future__ import annotations  # Anotaciones pospuestas.

from datetime import datetime  # Fecha/hora actual.

from sqlalchemy import Column, DateTime, Float, Integer, String  # Tipos y columnas ORM.

from app.db import Base  # Base declarativa compartida.


class Product(Base):  # Modelo de tabla products.
    """Tabla de productos.

    Campos comunes para inventario farmacéutico.
    """

    __tablename__ = "products"  # Nombre de la tabla en la BD.

    id = Column(Integer, primary_key=True, index=True)  # ID único.
    name = Column(String(120), nullable=False, index=True)  # Nombre del producto.
    description = Column(String(255), nullable=True)  # Descripción opcional.
    price = Column(Float, nullable=False)  # Precio.
    stock = Column(Integer, nullable=False, default=0)  # Stock disponible.
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)  # Fecha de creación.
