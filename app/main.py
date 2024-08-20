from fastapi import FastAPI
# from app.routers import auth
from app.routers import crm
from app.database.db import engine, Base
from sqlalchemy.orm import sessionmaker

# Создание экземпляра FastAPI
app = FastAPI()

# Подключение маршрутов
app.include_router(crm.router)

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)
