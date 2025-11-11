from fastapi.testclient import TestClient
from src.api.products import app

client = TestClient(app)

def test_product_crud():
    # CREATE
    response = client.post("/products", json={"name": "Laptop", "price": 999.99})
    assert response.status_code == 200
    product_id = response.json()["id"]

    # READ
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Laptop"
    assert data["price"] == 999.99