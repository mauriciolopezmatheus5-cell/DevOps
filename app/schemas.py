"""Esquemas Pydantic para validación y serialización."""

from __future__ import annotations  # Anotaciones pospuestas.

from datetime import datetime  # Tipo fecha/hora.
from typing import Optional  # Tipos opcionales.

from pydantic import BaseModel, ConfigDict, Field  # Base y validaciones.


class ProductBase(BaseModel):  # Esquema base de producto.
    """Campos base compartidos entre create y update."""

    name: str = Field(..., min_length=2, max_length=120)  # Nombre requerido.
    description: Optional[str] = Field(None, max_length=255)  # Descripción opcional.
    price: float = Field(..., gt=0)  # Precio mayor que 0.
    stock: int = Field(0, ge=0)  # Stock no negativo.


class ProductCreate(ProductBase):  # Payload de creación.
    """Datos requeridos para crear un producto."""

    pass  # No agrega campos extra.


class ProductUpdate(BaseModel):  # Payload de actualización.
    """Datos permitidos para editar un producto."""

    name: Optional[str] = Field(None, min_length=2, max_length=120)  # Nombre opcional.
    description: Optional[str] = Field(None, max_length=255)  # Descripción opcional.
    price: Optional[float] = Field(None, gt=0)  # Precio opcional.
    stock: Optional[int] = Field(None, ge=0)  # Stock opcional.


class ProductRead(ProductBase):  # Respuesta de lectura.
    """Respuesta de API para un producto."""

    id: int  # ID del producto.
    created_at: datetime  # Fecha de creación.

    model_config = ConfigDict(from_attributes=True)  # Permite leer desde ORM.
