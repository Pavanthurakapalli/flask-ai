from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
ma = Marshmallow()

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

    @app.route('/health')
    def health_check():
        return jsonify({"status": "ok", "message": "App is running"}), 200
    
    return app