import pytest


@pytest.fixture
def sample_product():
    """Return sample product data"""
    return {"name": "Laptop", "description": "Gaming Laptop", "price": 1200.99, "stock": 10}


def test_get_products_empty(client):
    """Test GET /products when no products exist"""
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json == []  # Should return an empty list


def test_add_product(client, sample_product):
    """Test POST /products to add a new product"""
    response = client.post("/products", json=sample_product)
    assert response.status_code == 201
    assert response.json["name"] == "Laptop"
    assert response.json["price"] == 1200.99


def test_get_products_non_empty(client, sample_product):
    """Test GET /products after adding a product"""
    client.post("/products", json=sample_product)
    response = client.get("/products")
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]["name"] == "Laptop"


def test_add_duplicate_product(client, sample_product):
    """Test adding a duplicate product (should return 409 conflict)"""
    client.post("/products", json=sample_product)  # First add
    response = client.post("/products", json=sample_product)  # Try duplicate
    assert response.status_code == 409
    assert "Product with this name already exists" in response.json["error"]


def test_add_product_invalid_data(client):
    """Test POST /products with invalid data"""
    invalid_product = {"name": "", "price": "invalid", "stock": -5}
    response = client.post("/products", json=invalid_product)
    assert response.status_code == 400
    assert "error" in response.json
