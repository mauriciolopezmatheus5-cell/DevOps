hola

## Cómo ejecutar los tests unitarios

### Opción 1: Local (venv activado)

- Asegúrate de tener el entorno virtual activado.
- Ejecuta los tests con pytest:

```
pytest -q
```

> Nota: los tests están en `tests/test_products.py`.

### Opción 2: Docker (PostgreSQL + tests)

Este comando levanta la base de datos, carga el SQL y ejecuta pytest:

```
docker compose up --build --abort-on-container-exit
```

Para limpiar contenedores y volumen:

```
docker compose down -v
```

## Cómo ejecutar la API

Ejecuta la app con Uvicorn:

```
uvicorn app.main:app --reload
```

Por defecto usa SQLite (`story.db`). Si quieres usar PostgreSQL, define:

```
export DATABASE_URL=postgresql+psycopg2://story_user:story_pass@localhost:5432/story
```

## Cómo llamar las APIs

Base URL (local): `http://127.0.0.1:8000`

### Listar productos (paginado por 3)

```
curl "http://127.0.0.1:8000/products"
```

### Listar con paginación y filtro por nombre

```
curl "http://127.0.0.1:8000/products?skip=0&limit=3&name=Paracetamol"
```

### Obtener producto por ID

```
curl "http://127.0.0.1:8000/products/1"
```

### Crear producto

```
curl -X POST "http://127.0.0.1:8000/products" \
	-H "Content-Type: application/json" \
	-d '{"name":"Ketorolaco 10mg","description":"Analgésico","price":5.25,"stock":33}'
```

### Editar producto

```
curl -X PUT "http://127.0.0.1:8000/products/1" \
	-H "Content-Type: application/json" \
	-d '{"price":6.00,"stock":40}'
```

### Eliminar producto

```
curl -X DELETE "http://127.0.0.1:8000/products/1"
```
