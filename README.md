# Test | Fast Api

Note api

## Table of Contents
+ [About](#about)
    + [Prerequisites](#prerequisites)
+ [Getting Started](#getting-started)
    + [Quickstart with docker-compose](#quickstart)
    + [Testing](#testing)
+ [Management commands](#management-commands)

## About <a name = "about"></a>
Note api backend server

### Prerequisites <a name = "prerequisites"></a>
```
Python 3.11.3
Postgres (inside container)
```
```
docker v20+
docker-compose v1.27+
```

## Getting Started <a name = "getting-started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Quickstart with docker-compose <a name = "quickstart"></a>

- Start conteinerized services
```bash
docker-compose up -d
```
- Installing dependencies
```bash
# Do it for the first time
pip install poetry

# Do it each time you would like to setup dependencies
poetry shell (or any other venv provider like Conda or other)
poetry install --no-root
poetry install --with dev
pre-commit install
```
- Copying configs
```
cp example.env .env
```
- Generate encryption key and salt. It is important to do this before migrate!
```
python
```

Server will start on localhost:8000


## Command-helpers for local development <a name = "management-commands"></a>

- `make help` - display available commands
- `make run` - run local developer server
- `make fmt` - run code auto-formatting
- `make lint` - run static code analyzers
