import os
from pydantic_settings import BaseSettings, SettingsConfigDict


ENV = os.environ.get("ENVIRONMENT") or 'example'

class Config(BaseSettings):
    model_config = SettingsConfigDict(env_file=f'.env.{ENV}')
    ENVIRONMENT: str = ENV 
    SERVER_HOST: str = '0.0.0.0'
    SERVER_PORT: str = '8000'

    DB_CONN_METHOD: str
    DB_HOSTNAME: str
    DB_DATABASE: str
    DB_USER: str
    DB_PASSWORD: str
    DB_ECHO: bool = False

config = Config()
    