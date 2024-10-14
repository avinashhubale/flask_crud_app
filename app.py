from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy, but don't bind it yet
db = SQLAlchemy()

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)
    
    # Configure the app
    app.config.from_object('config.Config')
    
    # Initialize the database with the app
    db.init_app(app)

    # Register blueprints
    from routes.user_routes import user_routes
    app.register_blueprint(user_routes)

    return app
