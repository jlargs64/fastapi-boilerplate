from sqlalchemy.orm import Session
from app.models.item import Item as ItemModel
from app.schemas.item import ItemCreate


class ItemService:
    @staticmethod
    def create_item(db: Session, item: ItemCreate):
        db_item = ItemModel(**item.dict())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def get_items(db: Session, skip: int = 0, limit: int = 100):
        return db.query(ItemModel).offset(skip).limit(limit).all()

    @staticmethod
    def get_item(db: Session, item_id: int):
        return db.query(ItemModel).filter(ItemModel.id == item_id).first()
