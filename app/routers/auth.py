from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.auth import User
from app.schemas.authSchemas import *

router = APIRouter(
    prefix="/api/v1/auth",
    tags=["auth"],
)


@router.post("/register/", response_model=UserBase)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.phone == user.phone).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Phone number already registered")

    if len(user.password) < 8:
        raise HTTPException(status_code=401, detail="Password must be at least 8 characters")
    # Создание нового пользователя и установка хешированного пароля
    new_user = User(phone=user.phone, name=user.name, surname=user.surname)
    new_user.set_password(user.password)

    db.add(new_user)
    db.commit()

    return {"username": new_user}

@router.post("/login/")
async def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.phone == user.phone).first()
    if not db_user or not db_user.verify_password(user.password):
        raise HTTPException(status_code=401, detail="Invalid phone number or password")

        # Возвращаем сообщение об успешном входе или токен
    return {"message": "Login successful"}
