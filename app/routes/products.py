from flask import Blueprint, request, jsonify
from app.models import product_schema, products_schema
from app.services.product_service import ProductService

products_bp = Blueprint("products", __name__)


@products_bp.route("/products", methods=["GET"])
def get_products():
    """Get all products"""
    products = ProductService.get_all_products()
    return products_schema.jsonify(products), 200


@products_bp.route("/products", methods=["POST"])
def add_product():
    """Add a new product"""
    data = request.get_json()

    # Validate request data
    errors = product_schema.validate(data)
    if errors:
        return jsonify({"error": errors}), 400

    # Check if product already exists
    if ProductService.get_product_by_name(data["name"]):
        return jsonify({"error": "Product with this name already exists"}), 409

    # Add new product
    new_product = ProductService.add_product(data)
    return product_schema.jsonify(new_product), 201
