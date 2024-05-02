from flask import Blueprint, request, jsonify
from flask_bcrypt import Bcrypt
from models.user_model import User
from sqlalchemy.exc import SQLAlchemyError

# Blueprint for user management
user_route = Blueprint('user_route', __name__)
bcrypt = Bcrypt()

# Register page

# Get method for all users data
@user_route.route('/register', methods=["GET"])
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