from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from models.user_model import User
from sqlalchemy.exc import SQLAlchemyError
from utils.db import db

# Blueprint for user management
user_routes = Blueprint('user_route', __name__)
bcrypt = Bcrypt()

# Register page

# Get method for all users data
@user_routes.route('/register', methods=["GET"])
def register_page():
    try:
        # Querying to get all users
        users = User.query.all()
        
        # Converting user data to JSON format
        users_data = []
        for user in users:
            user_data = {
                'id': user.id,
                'name': user.username,
                'email': user.email,
                'created_at': user.created_at,
                'updated_at': user.updated_at
            }
            users_data.append(user_data)
        
        # Returning user data as JSON
        return jsonify(users_data)
    except SQLAlchemyError as e:
        # Returning an error message if there is a database query error
        return jsonify({'error': 'Failed to fetch user data', 'message': str(e)}), 500
    
# Post method for registering a new user
@user_routes.route('/register', methods=["POST"])
def create_user():
    # Retrieving data from the request
    data = request.get_json()

    try:
        # Checking if the user already exists
        user_exists = User.query.filter_by(email=data['email']).first()
        if user_exists:
            return jsonify({'message': 'User already registered'}), 400

        # Encrypting password with bcrypt
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        # Creating a new user
        new_user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User successfully added'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Failed to add user', 'error': str(e)}), 500