from flask import request, jsonify
from marshmallow import ValidationError
from . import User
from userschema import UserSchema
from . import auth_bp
from app import db

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"error":"No input data provided"}), 400
    
    try:
        data = user_schema.load(data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    username = data['username']
    email = data['email']
    password = data['password']

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "username already exists"}), 409
    
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "email already exists"}), 409
    
    try:
        new_user = User(username=username, email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return jsonify(user_schema.dump(new_user)), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "An error occurred while creating the user.", "details": str(e)}), 500



    
