from app.extensions import db
from app.models import Order, Product
from sqlalchemy.exc import SQLAlchemyError


class OrderService:
    @staticmethod
    def place_order(order_data):
        """Place an order and validate stock levels."""
        products_requested = order_data["products"]  # Dict of {product_id: quantity}
        total_price = 0
        product_updates = []  # To track stock updates

        if not products_requested:
            return {"error": "Order must contain at least one product"}, 400

        # Check stock availability
        for product_id, quantity in products_requested.items():
            product = Product.query.get(product_id)
            if not product:
                return {"error": f"Product with ID {product_id} not found"}, 404

            if product.stock < quantity:
                return {"error": f"Insufficient stock for {product.name}"}, 400

            # Calculate total price
            total_price += product.price * quantity
            product_updates.append((product, quantity))

        try:
            # Deduct stock and create order
            for product, quantity in product_updates:
                product.stock -= quantity

            new_order = Order(products=products_requested, total_price=total_price, status="pending")
            db.session.add(new_order)
            db.session.commit()

            return new_order, 201

        except SQLAlchemyError:
            db.session.rollback()
            return {"error": "Database error while placing order"}, 500
