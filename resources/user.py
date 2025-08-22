# resources/user.py
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models import UserModel
from database import db

_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
_user_parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

class UserRegister(Resource):
    def post(self):
        data = _user_parser.parse_args()

        if UserModel.query.filter_by(username=data['username']).first():
            return {"message": "A user with that username already exists"}, 400

        hashed_password = generate_password_hash(data['password'])
        
        user = UserModel(username=data['username'], password_hash=hashed_password)
        db.session.add(user)
        db.session.commit()

        return {"message": "User created successfully."}, 201

class UserLogin(Resource):
    def post(self):
        data = _user_parser.parse_args()
        user = UserModel.query.filter_by(username=data['username']).first()

        if user and check_password_hash(user.password_hash, data['password']):
            # The fix is here: convert user.id to a string
            access_token = create_access_token(identity=str(user.id), fresh=True)
            return {'access_token': access_token}, 200

        return {'message': 'Invalid credentials'}, 401