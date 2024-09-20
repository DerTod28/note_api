# Test | Fast Api

Note api

![Документация](https://3.downloader.disk.yandex.com/preview/add1ba953b65165ae4ac45d41e77f4cbd2ab0e4a2db261ead5b993e6d600dfdd/inf/9RDZblOjIQZPbl839Sx7ksmfKtUilLChNzIdM1sO-9hbXBKf5w_AZGwFzI4QMqRxmC3sDfgcBOA90E4iT5WG5w%3D%3D?uid=1393619558&filename=%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202024-09-20%20%D0%B2%2003.07.52.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=1393619558&tknv=v2&size=2880x1558)
Документация -
http://127.0.0.1:8000/api/openapi#/

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
docker-compose v3.8
```

## Getting Started <a name = "getting-started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Quickstart with docker-compose <a name = "quickstart"></a>

- Start conteinerized services - prod (altogether)
```bash
docker-compose -f docker-compose.prod.yml build
docker-compose -f docker-compose.prod.yml up
```
or
- Start conteinerized services - dev (just postgres/redis)
```bash
docker-compose -f docker-compose.dev.yml up
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
- Start project
```
uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload
```

- Run worker (for Yandex api)
```
 celery -A app worker -l INFO
```

Server will start on localhost:8000


## Command-helpers for local development <a name = "management-commands"></a>

- `make help` - display available commands
- `make run` - run local developer server
- `make fmt` - run code auto-formatting
- `make lint` - run static code analyzers
