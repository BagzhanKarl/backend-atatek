from pydantic import BaseModel

class UserBase(BaseModel):
    id: int
    phone: str
    name: str
    surname: str

class UserCreate(BaseModel):
    phone: str
    name: str
    surname: str
    password: str

class UserLogin(BaseModel):
    phone: str
    password: str

    class Config:
        orm_mode = True
