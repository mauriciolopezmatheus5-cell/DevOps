# Imagen base con Python
FROM python:3.12-slim

# Evita que Python escriba .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Fuerza salida sin buffer en logs
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia requirements primero para cache
COPY requirements.txt /app/requirements.txt

# Instala dependencias del proyecto
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copia el resto del código
COPY . /app/

# Comando por defecto: ejecutar tests
CMD ["pytest", "-q"]
