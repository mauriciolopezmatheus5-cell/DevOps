"""Configuración de base de datos.

- Usa SQLAlchemy para conectar y manejar sesiones.
- Carga un script SQL con datos de ejemplo si la tabla está vacía.
"""

from __future__ import annotations  # Permite anotaciones pospuestas.

import os  # Acceso a variables de entorno.
from pathlib import Path  # Manejo de rutas de archivo.

from sqlalchemy import create_engine, text  # Crea el motor de BD y SQL textual.
from sqlalchemy.orm import declarative_base, sessionmaker  # Base ORM y fábrica de sesiones.

# URL de conexión. Por defecto usa SQLite en el archivo story.db
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./story.db")  # URL de conexión.

# Para SQLite se requiere esta opción de conexión
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}  # Args extra para SQLite.

engine = create_engine(DATABASE_URL, connect_args=connect_args)  # Motor principal de BD.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # Sesiones transaccionales.
Base = declarative_base()  # Base para declarar modelos.


def get_db():  # Dependencia de FastAPI para sesiones.
    """Dependencia de FastAPI para obtener una sesión de BD por request."""

    db = SessionLocal()  # Crea una sesión nueva.
    try:  # Inicio del bloque protegido.
        yield db  # Entrega la sesión al endpoint.
    finally:  # Se ejecuta siempre.
        db.close()  # Cierra la sesión.


def init_db() -> None:  # Inicializa tablas y datos.
    """Crea tablas y carga datos de ejemplo si no existen productos.

    Se ejecuta al iniciar la app.
    """

    # Importación tardía para evitar ciclos
    from app.models import Product  # Importa el modelo evitando ciclos.

    Base.metadata.create_all(bind=engine)  # Crea tablas si no existen.

    # Si la tabla ya tiene datos, no se reinsertan
    with SessionLocal() as db:  # Abre sesión temporal.
        try:  # Intenta consultar cantidad.
            count = db.query(Product).count()  # Cuenta registros.
        except Exception:  # Si falla la tabla.
            count = 0  # Asume sin datos.

    if count == 0:  # Solo inserta si está vacío.
        is_sqlite = DATABASE_URL.startswith("sqlite")  # Detecta motor SQLite.
        sql_file = "story.sql" if is_sqlite else "story_postgres.sql"  # Elige script.
        sql_path = Path(__file__).resolve().parents[1] / "data" / "sql" / sql_file  # Ruta del SQL.
        if sql_path.exists():  # Verifica existencia del archivo.
            if is_sqlite:  # Rama para SQLite.
                raw_conn = engine.raw_connection()  # Conexión de bajo nivel.
                try:  # Bloque protegido.
                    # executescript permite múltiples sentencias en SQLite
                    raw_conn.executescript(sql_path.read_text(encoding="utf-8"))  # Ejecuta SQL.
                    raw_conn.commit()  # Confirma cambios.
                finally:  # Se ejecuta siempre.
                    raw_conn.close()  # Cierra conexión.
            else:  # Rama para Postgres u otros motores.
                sql_text = sql_path.read_text(encoding="utf-8")  # Lee el SQL.
                statements = [s.strip() for s in sql_text.split(";") if s.strip()]  # Separa sentencias.
                with engine.begin() as conn:  # Abre transacción.
                    for stmt in statements:  # Recorre cada sentencia.
                        conn.execute(text(stmt))  # Ejecuta SQL.
