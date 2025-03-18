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

- **Configuración y ejecución correcta de Docker**:
  - Se utilizó Docker Compose para simplificar la configuración y ejecución de los servicios de la aplicación (API y base de datos MongoDB). Esto permite que ambos contenedores se ejecuten en la misma red automáticamente, facilitando la comunicación entre ellos.
  - Se definió un volumen para MongoDB (`./data:/data/db`) para garantizar la persistencia de los datos entre reinicios del contenedor.
  - Se utilizó `restart: always` para asegurar que los contenedores se reinicien automáticamente en caso de fallos o reinicios del sistema.

- **Manejo de variables de entorno con `.env`**:
  - Se utilizó un archivo `.env` para centralizar las configuraciones sensibles y específicas del entorno, como el puerto de la aplicación (`PORT`) y las credenciales de conexión a MongoDB (`MONGODB_URI` y `MONGODB_DB_NAME`). Esto permite una configuración más flexible y evita exponer información sensible directamente en el archivo `docker-compose.yml`.

- **Ejecución de pruebas automatizadas**:
  - Las pruebas automatizadas se ejecutan utilizando el comando:
    ```sh
    docker-compose run --rm app sh -c "PYTHONPATH=/app pytest"
    ```
    Esto permite ejecutar las pruebas en un contenedor aislado, asegurando que el entorno de pruebas sea consistente y reproducible.
  - **Decisión de no incluir las pruebas en el flujo de `docker-compose up`**:
    - Las pruebas no se integraron directamente en el flujo de `docker-compose up` porque este comando está diseñado para iniciar los servicios de la aplicación en un entorno de desarrollo o producción, no para ejecutar pruebas.
    - Separar las pruebas del flujo principal permite ejecutar los tests solo cuando sea necesario, sin afectar el despliegue de los servicios.
    - Esto también facilita la depuración, ya que las pruebas pueden ejecutarse de forma independiente y no interrumpen la ejecución de los contenedores principales.

- **Exposición y prueba de endpoints en FastAPI**:
  - Se utilizó Swagger UI, disponible en `http://localhost:${PORT:-8080}/docs`, para probar manualmente los endpoints de la API. Esto facilita la validación de las funcionalidades implementadas y la detección de errores en tiempo de desarrollo.

- **Uso de MongoDB para la persistencia de datos**:
  - MongoDB se configuró como base de datos para almacenar la información de los cursos. Se utilizó un volumen para garantizar la persistencia de los datos entre reinicios del contenedor.
  - Para facilitar la visualización de los datos, se recomendó el uso de MongoDB Compass como herramienta gráfica.

- **Pruebas Automatizadas**:
  - Se crearon pruebas utilizando `pytest` y `httpx` para validar el correcto funcionamiento de los endpoints, incluyendo pruebas para casos válidos e inválidos. Esto asegura que la API cumpla con los requisitos funcionales y maneje adecuadamente los errores.
---

## 🔧 Prerrequisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- **Python 3.11**
- **Docker** y **Docker Compose**
- Opcional: **MongoDB Compass**

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
http://localhost:${PORT:-8080}/docs
```
Si port es 8080, la URL será `http://localhost:8080/docs`.

Ahi mismo se pueden probar los endpoints al seleccionar la opcion `Try it out`. Luego, se deberá completar con el correspondiente `Request body`, y finalmente ejecutar la consulta con `Execute`. Esto permite observar la respuesta con su formato adecuado, junto al `Status code`.

Para la parte de los endpoints `GET /courses` y `GET /courses/{id}`, ademas de visualizarlos mediante `http://localhost:${PORT:-8080}/docs`, se puede acceder con los siguientes URL respectivamente: `localhost:${PORT:-8080}/courses` y `localhost:${PORT:-8080}/courses/{id}`.  

### Herramienta de Pruebas

Para más información sobre la herramienta de pruebas utilizada, visita el [repositorio de pytest de github](https://github.com/pytest-dev/pytest) o la [pagina oficial](https://docs.pytest.org/en/stable/).

## 📜 Logging

La aplicación genera logs detallados de operaciones y errores en el archivo `logs/app.log`. 

---