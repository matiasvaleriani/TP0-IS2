# TP0-IS2

# 📌 Tabla de Contenidos

- [Introducción](#introducción)
- [Desafíos del Proyecto](#desafíos-del-proyecto)
- [Pre-requisitos](#pre-requisitos)
- [Construcción y Ejecución con Docker](#construcción-y-ejecución-con-docker)
- [Base de Datos](#base-de-datos)
- [Testing](#testing)

---

## 📖 Introducción

Este proyecto es una API RESTful desarrollada con **FastAPI** en Python. La API permite gestionar "cursos" de manera sencilla utilizando almacenamiento en memoria. Su objetivo es servir como base para un trabajo práctico de la materia **Ingeniería de Software II**.

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

Para construir y ejecutar la imagen de Docker, sigue estos pasos:

### 1️⃣ Construir la imagen
```sh
 docker build -t mi-api .
```

### 2️⃣ Ejecutar el contenedor
```sh
 docker run -d -p 8080:8080 --env-file .env mi-api
```

### 3️⃣ Verificar que el contenedor esté corriendo
```sh
 docker ps
```

Para detener el contenedor en ejecución:
```sh
 docker stop <CONTAINER_ID>
```

---

## 🗄️ Base de Datos

Actualmente, la API almacena los datos en memoria. No se está utilizando una base de datos, pero en el futuro se podría integrar **MongoDB** o **PostgreSQL** según los requerimientos.

---

## 🧪 Testing

Aún no se han implementado pruebas automáticas. Una vez agregadas, se proporcionará el link a la herramienta utilizada para testear la API.

Para probar manualmente los endpoints, usa **Swagger UI** en:
```sh
http://localhost:8080/docs
```

