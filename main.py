from flask import Flask
from dotenv import load_dotenv
from utils.db import init_db
from controllers.user_management_route import user_routes
import os

# Create the application instance
app = Flask(__name__)

# Load the Configurations
load_dotenv()

# Setting database URI directly
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

# Initializing database
init_db(app)

#  Registering blueprints
app.register_blueprint(user_routes)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)