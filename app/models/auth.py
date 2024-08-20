from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import validates
from passlib.context import CryptContext
from app.database.db import Base
from passlib.context import CryptContext

# Создайте контекст для хеширования
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(25))
    permissions = Column(String(255))


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String(11), unique=True, index=True)
    password_hash = Column(String(255))
    name = Column(String(25))
    surname = Column(String(25))
    role = Column(Integer, default=1)

    def set_password(self, password: str):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password_hash)
