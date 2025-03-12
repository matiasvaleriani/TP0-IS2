from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.routes import router
from app.utils import ensure_data_file_exists

# Cargar variables del archivo .env
load_dotenv()

# Configuración de la aplicación
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8080))
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

app = FastAPI()

# Asegurarse de que el archivo de datos exista
ensure_data_file_exists()

# Incluir las rutas
app.include_router(router)