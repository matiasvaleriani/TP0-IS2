# 📌 TP0-IS2

## 📖 Introducción

Este proyecto es una API RESTful desarrollada con **FastAPI** en Python. La API permite gestionar "cursos" de manera sencilla utilizando almacenamiento en memoria.

---

## 🚀 Desafíos del Proyecto

Hasta el momento, los principales desafíos han sido:
- Configuración y ejecución correcta de Docker.
- Manejo de variables de entorno con `.env`.
- Exposición y prueba de los endpoints de FastAPI.

---

## 🔧 Pre-requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- **Python 3.11**
- **Docker** y **Docker Compose**

Si deseas probar los endpoints de la API, puedes utilizar **Swagger UI**, que se encuentra en `http://localhost:8080/docs`.

---

## 🐳 Construcción y Ejecución con Docker

Para construir y ejecutar la imagen de Docker utilizando Docker Compose, sigue estos pasos:

### 1️⃣ Construir y levantar el contenedor
```sh
docker-compose up --build -d
```

### 2️⃣ Verificar que el contenedor esté corriendo
```sh
 docker ps
```

### 3️⃣ Detener y eliminar el contenedor
```sh
 docker-compose down
```

---

## 🗄️ Base de Datos

Actualmente, la API almacena los datos en un archivo JSON dentro del contenedor. Los datos se persisten en la carpeta data en el directorio del proyecto, lo que asegura que los datos se mantengan entre reinicios del contenedor.

---

## 🧪 Testing

Aún no se han implementado pruebas automáticas. Una vez agregadas, se proporcionará el link a la herramienta utilizada para testear la API.

Para probar manualmente los endpoints, usa **Swagger UI** en:
```sh
http://localhost:8080/docs
```

