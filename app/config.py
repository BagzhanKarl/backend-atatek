from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()  # Загружаем переменные окружения из .env

class Settings(BaseSettings):
    database_url: str

settings = Settings()
