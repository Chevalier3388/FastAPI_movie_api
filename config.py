import os
from pydantic_settings import BaseSettings
from pydantic import SecretStr

from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", None)
    POSTGRES_PASSWORD: SecretStr = SecretStr(os.getenv("POSTGRES_PASSWORD", None))
    DB_HOST: str = os.getenv("DB_HOST", None)
    DB_NAME: str = os.getenv("DB_NAME", None)

    URL: str = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/'
    API_KEY: SecretStr = SecretStr(os.getenv("API_KEY", None))


    headers: dict = {
        'X-API-KEY': API_KEY.get_secret_value(),
        'Content-Type': 'application/json'
    }

    @property
    def database_url(self) -> str:
        return (f"postgresql+asyncpg://"
                f"{self.POSTGRES_USER}:"
                f"{self.POSTGRES_PASSWORD.get_secret_value()}@"
                f"{self.DB_HOST}:5432/"
                f"{self.DB_NAME}")



settings = Settings()

# print(settings.API_KEY.get_secret_value())
# print(settings.headers)