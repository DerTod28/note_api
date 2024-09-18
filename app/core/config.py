import os

from pydantic import Field
from pydantic_settings import BaseSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Settings(BaseSettings):
    PROJECT_NAME: str = 'FastAPI KODE notes Project'
    API_VERSION: str = Field(alias='API_VERSION')
    DATABASE_URL: str = Field(alias='DATABASE_URL')
    POSTGRES_USER: str = Field(alias='POSTGRES_USER')
    POSTGRES_SERVER: str = Field(alias='POSTGRES_SERVER', default='localhost')
    POSTGRES_PORT: str = Field(alias='POSTGRES_PORT', default=5432)  # default
    POSTGRES_PASSWORD: str = Field(alias='POSTGRES_PASSWORD')
    POSTGRES_DB: str = Field(alias='POSTGRES_DB')

    class Config:
        env_file = os.path.join(BASE_DIR, '.env')
        env_file_encoding = 'utf-8'


settings = Settings()  # type: ignore[call-arg]


def get_db_url() -> str:
    return (
        f'postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@'
        f'{settings.POSTGRES_SERVER}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}'
    )
