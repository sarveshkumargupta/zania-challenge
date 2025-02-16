import pytest
from app import create_app
from app.extensions import db


@pytest.fixture
def app():
    """Create a Flask test app"""
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",  # Use in-memory DB for tests
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })

    with app.app_context():
        db.create_all()  # Create tables for testing
        yield app
        db.session.remove()
        db.drop_all()  # Clean up after tests


@pytest.fixture
def client(app):
    """Create a test client"""
    return app.test_client()
