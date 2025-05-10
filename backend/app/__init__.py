from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import SQLALCHEMY_DATABASE_URI

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")
    CORS(app)
    db.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
