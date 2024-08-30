# Financial Transaction API with FastAPI, Poetry, and SQLite

This project is a RESTful API for managing financial transactions, built with FastAPI, using Poetry for dependency management and SQLite as the database.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)

## Features

- FastAPI for building high-performance APIs
- Poetry for dependency management and packaging
- SQLite for lightweight, serverless database operations
- Pydantic for data validation and settings management

## Getting Started

### Prerequisites

- Python 3.12+
- Poetry

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/MielAndMoon/finance-api.git
   cd finance-api
   ```

2. Install dependencies using Poetry:

   ```
   poetry install
   ```

### Running the Application

1. Activate the virtual environment:
   ```
   poetry shell
   ```

2. Run the FastAPI server:
   ```
   uvicorn app.main:app --reload
   ```

The API will be available at `http://localhost:8000`.

### API Documentation

FastAPI provides automatic interactive API documentation. After starting the application, you can access:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Project Structure

```
.
├── app
│   ├── api.py
│   ├── database.py
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── service.py
├── poetry.lock
├── pyproject.toml
├── README.md
├── .gitignore
└── tests
    └── __init__.py
```

### API Endpoints

The API provides the following endpoints for managing financial transactions:

- `GET /transactions`: List all transactions
- `POST /transactions`: Create a new transaction
