# 📌 Trabajo Practico Individual Ingenieria de Software II

## 📚 Tabla de Contenidos

1. [Introducción](#📖-introducción)
2. [Desafíos del Proyecto](#🚀-desafíos-del-proyecto)
3. [Pre-requisitos](#🔧-pre-requisitos)
4. [Construcción y Ejecución con Docker](#🐳-construcción-y-ejecución-con-docker)
5. [Base de Datos](#🗄️-base-de-datos)
6. [Testing](#🧪-testing)

## 📖 Introducción

Este proyecto consiste en una API RESTful desarrollada con FastAPI en Python, cuyo propósito es permitir la gestión de cursos dentro de la plataforma ClassConnect. La API proporciona funcionalidades para crear, visualizar y eliminar cursos, utilizando una estructura de almacenamiento en memoria. Se implementaron las mejores prácticas en cuanto a manejo de errores siguiendo el estándar RFC 7807, ejecución dentro de un entorno Dockerizado, y pruebas automáticas con pytest para garantizar la calidad del software.

---

## 🚀 Desafíos del Proyecto

Durante el desarrollo del proyecto, se presentaron varios desafíos técnicos y conceptuales:

- Configuración y ejecución correcta de Docker.
- Manejo de variables de entorno con `.env`.
- Exposición y prueba de los endpoints de FastAPI.
- Persistencia en Memoria.
- Pruebas Automatizadas: Se crearon pruebas utilizando pytest y httpx para validar el correcto funcionamiento de los endpoints, incluyendo pruebas de casos válidos e inválidos.

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

### Pruebas Automáticas

Para ejecutar las pruebas automáticas, usa el siguiente comando:
```sh
docker-compose run --rm tests
```

### Pruebas Manuales

Para probar manualmente los endpoints, usa **Swagger UI** en:
```sh
http://localhost:8080/docs
```

### Herramienta de Testing

Para más información sobre la herramienta de testing utilizada, visita el [repositorio de pytest](https://github.com/pytest-dev/pytest) o la [pagina oficial](https://docs.pytest.org/en/stable/)

---
