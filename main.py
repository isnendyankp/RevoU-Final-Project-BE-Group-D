from flask import Flask
from flask_jwt_extended import JWTManager
from utils.db import init_db
from controllers.user_management_route import user_routes
from dotenv import load_dotenv
import os
from flask_cors import CORS


# Create the application instance
app = Flask(__name__)

CORS(app)

# Load the Configurations
load_dotenv()

# Setting database URI directly
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:RwpRYvCgwTIqjgoUQDPBMnCVpPLxudri@roundhouse.proxy.rlwy.net:47006/railway"

# Initializing database
init_db(app)

# Setting JWT secret key directly
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
jwt = JWTManager(app)

#  Registering blueprints
app.register_blueprint(user_routes)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)