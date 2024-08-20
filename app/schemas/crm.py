from pydantic import BaseModel

class ItemCreate(BaseModel):
    phone: str
    name: str
    type: str

class ItemBase(BaseModel):
    id: int
    phone: str
    name: str
    type: str