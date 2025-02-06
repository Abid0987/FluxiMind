from flask import Flask

def create_app():
    """
    Factory function to create and configure the Flask app.
    """
    app = Flask(__name__)

    # Load configuration settings
    from app.config import Config
    app.config.from_object(Config)

    # Register Blueprints
    from app.routes.chat_routes import chat_routes
    app.register_blueprint(chat_routes)

    return app