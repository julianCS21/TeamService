# src/core/config.py
from pydantic import BaseSettings


class Settings(BaseSettings):
    api_football_key: str
    base_football_url: str
    port: int = 8000

    class Config:
        env_file = ".env"
