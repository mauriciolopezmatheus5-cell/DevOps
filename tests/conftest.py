"""Configuración global de pytest.

Se asegura de que el paquete `app` sea importable.
"""

from __future__ import annotations  # Anotaciones pospuestas.

import sys  # Acceso a sys.path.
from pathlib import Path  # Manejo de rutas.

# Ruta raíz del proyecto (carpeta que contiene /app y /tests)
PROJECT_ROOT = Path(__file__).resolve().parents[1]  # Calcula la raíz.

# Inserta la raíz al inicio del path si no existe
if str(PROJECT_ROOT) not in sys.path:  # Verifica si ya está.
    sys.path.insert(0, str(PROJECT_ROOT))  # Agrega para resolver imports.
