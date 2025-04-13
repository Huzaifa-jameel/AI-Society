from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os

csrf = CSRFProtect()

def create_app():
    # Get the absolute path to the project root (AI-SOCIETY folder)
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    
    app = Flask(__name__,
                template_folder=os.path.join(base_dir, 'templates'),
                static_folder=os.path.join(base_dir, 'static'))
    
    # Configuration
    app.config.from_pyfile(os.path.join(base_dir, 'config_global.py'))
    
    # Load instance config if exists
    instance_config = os.path.join(base_dir, 'instance', 'config.py')
    if os.path.exists(instance_config):
        app.config.from_pyfile(instance_config)
    
    # Initialize CSRF
    csrf.init_app(app)
    
    # Register blueprints
    from app import routes
    app.register_blueprint(routes.bp)
    
    return app