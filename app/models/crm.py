from sqlalchemy import Column, Integer, String
from app.database.db import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String(11), unique=True, index=True)
    name = Column(String(25), nullable=False)
    type = Column(String(255), nullable=False)

