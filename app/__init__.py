from flask import Flask
from app.extensions import db, migrate, ma
from app.routes.products import products_bp
from app.routes.orders import orders_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    # Import models to ensure they are registered with SQLAlchemy
    from app import models

    # Register blueprints
    app.register_blueprint(products_bp)
    app.register_blueprint(orders_bp)

    return app
