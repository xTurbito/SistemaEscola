# app/__init__.py

from flask import Flask
from app.controllers.auth_controller import auth_bp
from app.controllers.campus_controller import campus_bp
from app.controllers.licenciaturas_controller import licenciaturas_bp
from app.controllers.panel_controller import panel_bp

def create_app():
    app = Flask(__name__)
    app.secret_key = 'mysecretkey'
    
    # Registrar Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(campus_bp)
    app.register_blueprint(licenciaturas_bp)
    app.register_blueprint(panel_bp)
    
    return app
