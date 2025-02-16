from flask import Blueprint, request, jsonify
from app.models import order_schema
from app.services.order_service import OrderService

orders_bp = Blueprint("orders", __name__)


@orders_bp.route("/orders", methods=["POST"])
def place_order():
    """Handle order placement"""
    data = request.get_json()

    # Validate request payload
    if not data or "products" not in data or not isinstance(data["products"], dict):
        return jsonify({"error": "Invalid request format. Expected {'products': {product_id: quantity}}" }), 400

    # Process the order
    result, status_code = OrderService.place_order(data)

    if status_code >= 400:
        return jsonify(result), status_code
    
    return order_schema.jsonify(result), status_code
