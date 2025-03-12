from fastapi import FastAPI
from app.routes import router
from app.utils import ensure_data_file_exists

app = FastAPI()

# Asegurarse de que el archivo de datos exista
ensure_data_file_exists()

# Incluir las rutas
app.include_router(router)