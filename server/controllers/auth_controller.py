from flask import Blueprint, request
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from server.extensions import db

from server.models.user import User

auth_bp = Blueprint("auth", __name__)
auth_api = Api(auth_bp)


class RegisterAPI(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return {"error": "Username and password requires"}, 400
        
        if User.query.filter_by(username=username).first():
            return {"error": "Username already exists"}, 400
        
        user = User(username=username)
        user.password = password
        
        db.session.add(user)
        db.session.commit()

        return {"message": "User registered successfully"}, 201
    

class LoginAPI(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()

        if not user or not user.check_password(password):
            return {"error": "Invalid credentials"}, 401
        
        access_token = create_access_token(identity=user.id)
        return {"access_token": access_token}, 200
    

class ProfileAPI(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        return {"id": user.id, "username": user.username}, 200
    
auth_api.add_resource(RegisterAPI, "/register")
auth_api.add_resource(LoginAPI, "/login")
auth_api.add_resource(ProfileAPI, "/profile")