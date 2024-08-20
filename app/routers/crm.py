from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.crm import Item
from app.database.db import get_db
from app.schemas.crm import ItemCreate, ItemBase

router = APIRouter(
    prefix="/api/v1/crm",
    tags=["CRM"],
)


@router.post("/add/")
async def add_item(item: ItemCreate, db: Session = Depends(get_db)):
    new_item = Item(phone=item.phone, name=item.name, type=item.type)
    db.add(new_item)
    db.commit()
    return {"status": True}

@router.post("/count/{itemname}")
async def get_item_count(itemname: str, db: Session = Depends(get_db)):
    item_count = db.query(Item).filter(Item.type == itemname).count()
    return {"status": True, "count": item_count}