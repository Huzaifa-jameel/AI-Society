import os
from dotenv import load_dotenv

load_dotenv('file.env')

class Config:
    # Required configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-fallback-key-123')
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.getenv('SECRET_KEY', 'different-csrf-secret-456')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}