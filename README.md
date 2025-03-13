# 📌 Individual - Software Engineering II

## 📚 Table of Contents

1. [Introduction](#📖-introduction)
2. [Project Challenges](#🚀-project-challenges)
3. [Prerequisites](#🔧-prerequisites)
4. [Building and Running with Docker](#🐳-building-and-running-with-docker)
5. [Database](#🗄️-database)
6. [Testing](#🧪-testing)
7. [Logging](#📜-logging)

## 📖 Introduction

This project consists of a RESTful API developed with FastAPI in Python, aimed at managing courses within the ClassConnect platform. The API provides functionalities to create, view, and delete courses, using MongoDB for data storage. Best practices were implemented regarding error handling following the RFC 7807 standard, execution within a Dockerized environment, and automated testing with pytest to ensure software quality.

---

## 🚀 Project Challenges

During the development of the project, several technical and conceptual challenges were encountered:

- Correct configuration and execution of Docker.
- Handling environment variables with `.env`.
- Exposing and testing FastAPI endpoints.
- Using MongoDB for data persistence.
- Automated Testing: Tests were created using pytest and httpx to validate the correct functioning of the endpoints, including tests for valid and invalid cases.

---

## 🔧 Prerequisites

Before running the project, make sure you have installed:

- **Python 3.11**
- **Docker** and **Docker Compose**
- Optional: **MongoDB Compass**

If you want to test the API endpoints, you can use **Swagger UI**, which is available at `http://localhost:8080/docs`.

---

## 🐳 Building and Running with Docker

To build and run the Docker image using Docker Compose, follow these steps:

### 1️⃣ Build and start the container
```sh
docker-compose up --build -d
```

### 2️⃣ Verify that the container is running
```sh
docker ps
```

### 3️⃣ Stop and remove the container
```sh
docker-compose down
```

---

## 🗄️ Database

Currently, the API uses MongoDB as the database. The data is stored in the `data` folder in the project directory, ensuring that the data is retained between container restarts.

To view the database, you can use MongoDB Compass:

1. **Download and install MongoDB Compass** from [here](https://www.mongodb.com/try/download/compass).
2. **Open MongoDB Compass**.
3. **Connect to your MongoDB instance** by entering the following connection string:
```sh
mongodb://localhost:27017
```
4. **Click "Connect".**

---

## 🧪 Testing

### Automated Tests

To run the automated tests, use the following command:
```sh
docker-compose run --rm app sh -c "PYTHONPATH=/app pytest"
```

### Manual Tests

To manually test the endpoints, use **Swagger UI** at:
```sh
http://localhost:8080/docs
```

### Testing Tool

For more information about the testing tool used, visit the [pytest repository](https://github.com/pytest-dev/pytest) or the [official page](https://docs.pytest.org/en/stable/).

## 📜 Logging

The application generates detailed logs of operations and errors in the `logs/app.log` file. 

---