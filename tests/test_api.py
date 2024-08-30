def test_read_main(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to my FastAPI app with SQLite!"}


def test_create_item(test_client):
    item_data = {"name": "Test Item", "price": 10.5}
    response = test_client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"
    assert response.json()["price"] == 10.5
    assert "id" in response.json()


def test_read_items(test_client):
    response = test_client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_read_item(test_client):
    response = test_client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"


def test_read_item_not_found(test_client):
    response = test_client.get("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"
