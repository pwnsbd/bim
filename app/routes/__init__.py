# app/routes/__init__.py
from flask import Flask
from .main import main_bp
from .uploads import uploads_bp


def init_app(app: Flask):
    app.register_blueprint(main_bp)
    app.register_blueprint(uploads_bp)
