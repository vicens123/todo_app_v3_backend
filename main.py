from functools import lru_cache
from typing import Union
from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

import config  # importa la clase Settings
from routers import todos  # importa el router real de todos

# Cachear la configuración
default_settings = lru_cache()(lambda: config.Settings())

app = FastAPI(
    title="To-Do API",
    description="API para gestionar tareas",
    version="1.0.0"
)

# CORS para desarrollo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Manejador de errores HTTP
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

# Dependencia para settings cacheados
def get_settings():
    return default_settings()

# Ruta raíz
@app.get("/")
def read_root(settings: config.Settings = Depends(get_settings)):
    print(settings.app_name)
    return {"message": "Hello World", "app": settings.app_name}

# Endpoint con parámetro dinámico
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# Rutas de la API /todos
app.include_router(todos.router, prefix="", tags=["Todos"])
