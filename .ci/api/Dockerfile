# Stage 1: Build stage for dependencies
ARG IMAGE_NAME=tiangolo/uvicorn-gunicorn-fastapi:python3.11-slim
FROM ${IMAGE_NAME} as requirements-stage

# Set working directory
WORKDIR /app
COPY pyproject.toml poetry.lock /app/

# Set the poetry version and install it
ENV POETRY_VERSION=1.8.3
RUN pip install "poetry==${POETRY_VERSION}"

# Export dependencies to requirements.txt
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# Stage 2: Final stage to run the app
FROM ${IMAGE_NAME}
ENV WORKDIR_NAME=app

# Set working directory for the final stage
WORKDIR /

# Copy the requirements.txt from the previous stage
COPY --from=requirements-stage /app/requirements.txt /${WORKDIR_NAME}/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r /${WORKDIR_NAME}/requirements.txt

# Copy the FastAPI application code
COPY ./app /${WORKDIR_NAME}

# Expose port 8000 and define the command to run the app
EXPOSE 8000

# Command to run the FastAPI application using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
