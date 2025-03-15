# 📌 Individual - Ingeniería de Software II

## 📚 Tabla de Contenidos

1. [Introducción](#📖-introducción)
2. [Desafíos del Proyecto](#🚀-desafíos-del-proyecto)
3. [Prerrequisitos](#🔧-prerrequisitos)
4. [Construcción y Ejecución con Docker](#🐳-construcción-y-ejecución-con-docker)
5. [Base de Datos](#🗄️-base-de-datos)
6. [Testing](#🧪-testing)
7. [Logging](#📜-logging)

## 📖 Introducción

Este proyecto consiste en una API RESTful desarrollada con FastAPI en Python, destinada a la gestión de cursos dentro de la plataforma ClassConnect. La API proporciona funcionalidades para crear, visualizar y eliminar cursos, utilizando MongoDB para el almacenamiento de datos. Se implementaron buenas prácticas en cuanto al manejo de errores siguiendo el estándar RFC 7807, ejecución en un entorno Dockerizado y pruebas automatizadas con pytest para garantizar la calidad del software.

---

## 🚀 Desafíos del Proyecto

Durante el desarrollo del proyecto, se encontraron varios desafíos técnicos y conceptuales:

- Configuración y ejecución correcta de Docker.
- Manejo de variables de entorno con `.env`.
- Exposición y prueba de endpoints en FastAPI.
- Uso de MongoDB para la persistencia de datos.
- Pruebas Automatizadas: Se crearon pruebas utilizando pytest y httpx para validar el correcto funcionamiento de los endpoints, incluyendo pruebas para casos válidos e inválidos.

---

## 🔧 Prerrequisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- **Python 3.11**
- **Docker** y **Docker Compose**
- Opcional: **MongoDB Compass**

Si deseas probar los endpoints de la API, puedes usar **Swagger UI**, disponible en `http://localhost:8080/docs`.

---

## 🐳 Construcción y Ejecución con Docker

Para construir y ejecutar la imagen de Docker utilizando Docker Compose, sigue estos pasos:

### 1️⃣ Construir e iniciar el contenedor
```sh
docker-compose up --build -d
```

### 2️⃣ Verificar que el contenedor esté en ejecución
```sh
docker ps
```

### 3️⃣ Detener y eliminar el contenedor
```sh
docker-compose down
```

---

## 🗄️ Base de Datos

Actualmente, la API utiliza MongoDB como base de datos. Los datos se almacenan en la carpeta data dentro del directorio del proyecto, asegurando que los datos se conserven entre reinicios del contenedor.

Para visualizar la base de datos, se puede utilizar MongoDB Compass:

1. **Descarga e instala MongoDB Compass** desde [here](https://www.mongodb.com/try/download/compass).
2. **Abrir MongoDB Compass**.
3. **Conectar a la instancia de MongoDB** ingresando a la siguiente conexión:
```sh
mongodb://localhost:27017
```
4. **Conectar**.

---

## 🧪 Testing

### Pruebas Automatizadas

Para ejecutar las pruebas automatizadas, utiliza el siguiente comando:
```sh
docker-compose run --rm app sh -c "PYTHONPATH=/app pytest"
```

### Pruebas Manuales

Para probar manualmente los endpoints, se puede utilizar Swagger UI en:
```sh
http://localhost:8080/docs
```

### Herramienta de Pruebas

Para más información sobre la herramienta de pruebas utilizada, visita el [repositorio de pytest de github](https://github.com/pytest-dev/pytest) o la [pagina oficial](https://docs.pytest.org/en/stable/).

## 📜 Logging

La aplicación genera logs detallados de operaciones y errores en el archivo `logs/app.log`. 

---