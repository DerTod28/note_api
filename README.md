# Test | Fast Api

Note api

Документация
![Image alt](https://github.com/DerTod28/note_api/raw/main/documentation/images/01.png)


## Table of Contents
+ [About](#about)
    + [Prerequisites](#prerequisites)
+ [Getting Started](#getting-started)
    + [Quickstart with docker-compose](#quickstart)
    + [Testing](#testing)
+ [Management commands](#management-commands)

```
Список ручек:

- api/v1/users/create - Регистрация нового пользователя
- api/v1/auth/login - Выдача access token для последующих запросов
- api/v1/users/me [+ access] - Информация о текущем пользователе
- api/v1/notes/ [+ access] - Все заметки текущего пользователя
- api/v1/notes/{note_uid} [+ access] - Данные по конкретной заметке
- api/v1/notes/create [+ access] - Создание новой заметки. При сохранении запускается celery
таска, которая при необходимости корректирует текст и сохраняет его после исправлений.
  (после /notes/create можно взять uid записи и проверить результат Яндекс.Спелинга по запросу /notes/{note_uid})
```
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
