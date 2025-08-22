# resources/job.py
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import JobModel
from database import db

class Job(Resource):
    def get(self, job_id):
        job = JobModel.query.get_or_404(job_id)
        return {
            'id': job.id,
            'title': job.title,
            'description': job.description,
            'company': job.company,
            'author_id': job.user_id
        }

class JobList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title', type=str, required=True, help="Title cannot be blank")
    parser.add_argument('description', type=str, required=True, help="Description cannot be blank")
    parser.add_argument('company', type=str, required=True, help="Company cannot be blank")

    def get(self):
        jobs = JobModel.query.all()
        return {'jobs': [
            {
                'id': job.id,
                'title': job.title,
                'description': job.description,
                'company': job.company
            } for job in jobs
        ]}

    @jwt_required()
    def post(self):
        data = self.parser.parse_args()
        current_user_id = get_jwt_identity()
        
        new_job = JobModel(
            title=data['title'],
            description=data['description'],
            company=data['company'],
            user_id=int(current_user_id)
        )
        db.session.add(new_job)
        db.session.commit()
        return {'message': 'Job created successfully.', 'job_id': new_job.id}, 201