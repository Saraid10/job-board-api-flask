# app.py
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv

# Import from the database.py file
from database import db
from resources.user import UserRegister, UserLogin
from resources.job import Job, JobList
from resources.application import Application, ApplicationList

load_dotenv()

app = Flask(__name__)
api = Api(app)

# --- Configuration ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

# --- Add API Endpoints ---
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(Job, '/job/<int:job_id>')
api.add_resource(JobList, '/jobs')
api.add_resource(Application, '/job/<int:job_id>/apply')
api.add_resource(ApplicationList, '/job/<int:job_id>/applications')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
