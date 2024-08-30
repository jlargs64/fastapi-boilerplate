from sqlalchemy.orm import Session
from app.services.item_service import ItemService
from app.schemas.item import ItemCreate


def test_create_item(db: Session):
    item_create = ItemCreate(name="Test Item", price=10.5)
    item = ItemService.create_item(db, item_create)
    assert item.name == "Test Item"
    assert item.price == 10.5
    assert item.id is not None


def test_get_items(db: Session):
    # Create some test items
    ItemService.create_item(db, ItemCreate(name="Item 1", price=10.5))
    ItemService.create_item(db, ItemCreate(name="Item 2", price=20.5))

    items = ItemService.get_items(db)
    assert len(items) >= 2
    assert any(item.name == "Item 1" for item in items)
    assert any(item.name == "Item 2" for item in items)


def test_get_item(db: Session):
    # Create a test item
    created_item = ItemService.create_item(db, ItemCreate(name="Test Item", price=10.5))

    # Retrieve the item
    item = ItemService.get_item(db, created_item.id)
    assert item is not None
    assert item.name == "Test Item"
    assert item.price == 10.5


def test_get_non_existent_item(db: Session):
    item = ItemService.get_item(db, 999)  # Assuming 999 is not a valid ID
    assert item is None
