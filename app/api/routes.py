from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.item import Item, ItemCreate
from app.services.item_service import ItemService

router = APIRouter()


@router.post("/items/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return ItemService.create_item(db, item)


@router.get("/items/", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return ItemService.get_items(db, skip, limit)


@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = ItemService.get_item(db, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
