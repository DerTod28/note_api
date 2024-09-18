# Use official FastAPI base image
ARG IMAGE_NAME=tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim
FROM ${IMAGE_NAME} as requirements-stage
# Set working directory
WORKDIR /app
COPY pyproject.toml poetry.lock /app/

ENV POETRY_VERSION=1.8.3
RUN pip install "poetry==${POETRY_VERSION}"
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
FROM ${IMAGE_NAME}
ENV WORKDIR_NAME=app

WORKDIR /

COPY --from=requirements-stage /tmp/requirements.txt /${WORKDIR_NAME}/requirements.txt
RUN pip install --no-cache-dir -r /${WORKDIR_NAME}/requirements.txt

# Copy the FastAPI application code
COPY ./app /${WORKDIR_NAME}

# Expose port 8000 and define the command to run the app
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
