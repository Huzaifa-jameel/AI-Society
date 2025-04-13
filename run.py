import os
from app import create_app
from dotenv import load_dotenv

# Load environment variables
load_dotenv('file.env')  # Specify your .env file path

app = create_app()

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5023)),
        debug=os.environ.get('FLASK_ENV') == 'development'
    )