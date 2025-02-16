import json
import pytest
from app.extensions import db
from app.models import Product


@pytest.fixture
def setup_products(app):
    """Fixture to add test products to the database"""
    with app.app_context():
        product1 = Product(id=1, name="Laptop", description="A powerful laptop", price=1000.0, stock=5)
        product2 = Product(id=2, name="Phone", description="A smart phone", price=500.0, stock=3)
        db.session.add_all([product1, product2])
        db.session.commit()


@pytest.mark.usefixtures("setup_products")
def test_place_order_success(client):
    """Test successful order placement"""
    order_data = {
        "products": {
            "1": 2,
            "2": 1
        }
    }
    response = client.post("/orders", data=json.dumps(order_data), content_type="application/json")

    assert response.status_code == 201
    data = response.get_json()
    assert "id" in data
    assert data["total_price"] == 2500.0  # 2 * 1000 + 1 * 500
    assert data["status"] == "pending"


@pytest.mark.usefixtures("setup_products")
def test_place_order_insufficient_stock(client):
    """Test order placement fails due to insufficient stock"""
    order_data = {
        "products": {
            "1": 10  # More than available stock
        }
    }
    response = client.post("/orders", data=json.dumps(order_data), content_type="application/json")

    assert response.status_code == 400
    data = response.get_json()
    assert "error" in data
    assert "Insufficient stock" in data["error"]


@pytest.mark.usefixtures("setup_products")
def test_place_order_invalid_product(client):
    """Test order placement fails when ordering a non-existent product"""
    order_data = {
        "products": {
            "99": 1  # Non-existent product ID
        }
    }
    response = client.post("/orders", data=json.dumps(order_data), content_type="application/json")

    assert response.status_code == 404
    data = response.get_json()
    assert "error" in data
    assert "Product with ID 99 not found" in data["error"]
