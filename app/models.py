from app.extensions import db, ma


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)


# Defining the marshamallow schema for serialization and deserialization of Product
class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Product
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field()
    description = ma.auto_field()
    price = ma.auto_field()
    stock = ma.auto_field()


# Instance of product schemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    total_price = db.Column(db.Float, nullable=False, default=0.0)
    status = db.Column(db.String(20), nullable=False, default="pending")
    products = db.Column(db.JSON, nullable=False)  # Storing product IDs & quantities as JSON


# Defining the marshamallow schema for serialization and deserialization of Order
class OrderSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True

    id = ma.auto_field()
    total_price = ma.auto_field()
    status = ma.auto_field()
    products = ma.auto_field()


# Instance of product schemas
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)