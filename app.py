from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from config import Config
from flask_migrate import Migrate
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
ma = Marshmallow()
migrate = Migrate()

def create_app(config_class=Config):
    """
    Application factory pattern.
    Initializes and configures the Flask application.

    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    
    bcrypt.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    from auth.models import User


    from auth.routes import auth_bp  # Import the blueprint from auth.routes
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    

    @app.route('/health')
    def health_check():
        return jsonify({"status": "ok", "message": "App is running"}), 200
    
    return app