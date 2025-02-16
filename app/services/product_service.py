from app.extensions import db
from app.models import Product


class ProductService:
    @staticmethod
    def get_all_products():
        """Fetchs all products from the db"""
        return Product.query.all()

    @staticmethod
    def get_product_by_name(name):
        """Find a product by name"""
        return Product.query.filter_by(name=name).first()

    @staticmethod
    def add_product(data):
        """Add a new product"""
        new_product = Product(
            name=data["name"],
            description=data.get("description", ""),
            price=float(data["price"]),
            stock=int(data["stock"])
        )
        db.session.add(new_product)
        db.session.commit()
        return new_product
