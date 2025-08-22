# resources/application.py
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import ApplicationModel, JobModel
from database import db

class Application(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('applicant_name', type=str, required=True, help="Applicant name cannot be blank")
    parser.add_argument('applicant_email', type=str, required=True, help="Applicant email cannot be blank")

    @jwt_required()
    def post(self, job_id):
        if not JobModel.query.get(job_id):
            return {'message': 'Job not found'}, 404

        data = self.parser.parse_args()

        new_application = ApplicationModel(
            applicant_name=data['applicant_name'],
            applicant_email=data['applicant_email'],
            job_id=job_id
        )
        db.session.add(new_application)
        db.session.commit()
        return {'message': 'Application submitted successfully'}, 201

class ApplicationList(Resource):
    @jwt_required()
    def get(self, job_id):
        job = JobModel.query.get_or_404(job_id)
        current_user_id = get_jwt_identity()

        # Add these two print statements for debugging
        print(f"--- JOB CREATED BY USER ID: {job.user_id} (type: {type(job.user_id)}) ---")
        print(f"--- CURRENT LOGGED-IN USER ID: {current_user_id} (type: {type(current_user_id)}) ---")

        # The security check
        if str(job.user_id) != current_user_id:
            return {'message': 'You are not authorized to view these applications.'}, 403


        applications = ApplicationModel.query.filter_by(job_id=job_id).all()

        if not applications:
            return {'message': 'No applications found for this job.'}, 404

        return {'applications': [
            {
                'id': app.id,
                'applicant_name': app.applicant_name,
                'applicant_email': app.applicant_email,
                'applied_date': app.applied_date.isoformat()
            } for app in applications
        ]}