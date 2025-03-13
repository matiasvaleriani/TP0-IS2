from loguru import logger
import sys
import os

# Crear el directorio de logs si no existe
log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configuración básica de loguru
logger.remove()  # Elimina cualquier configuración previa
logger.add(sys.stdout, format="{time} {level} {message}", level="INFO")
logger.add(
    f"{log_directory}/app.log", rotation="1 MB", retention="10 days", level="DEBUG"
)


# Función para obtener el logger configurado
def get_logger():
    return logger
