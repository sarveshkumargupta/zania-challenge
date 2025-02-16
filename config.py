import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Using absolute path if env var is not configured
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'ecommerce.db')}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
