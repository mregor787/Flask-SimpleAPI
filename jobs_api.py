from flask import jsonify, Blueprint, request

from data import db_session
from data.jobs import Jobs

blueprint = Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return jsonify({
        'jobs': [job.to_dict(only=(
            'id', 'job', 'work_size', 'collaborators', 'start_date',
            'end_date', 'is_finished', 'team_leader'
        )) for job in jobs]
    })


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify({
        'job': job.to_dict(only=(
            'id', 'job', 'work_size', 'collaborators', 'start_date',
            'end_date', 'is_finished', 'team_leader'
        ))
    })


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    keys = [
        'id', 'job', 'work_size', 'collaborators', 'start_date',
        'end_date', 'is_finished', 'team_leader'
    ]
    if not all(key in request.json for key in keys):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    job = Jobs(
        id=request.json['id'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        start_date=request.json['start_date'],
        end_date=request.json['end_date'],
        is_finished=request.json['is_finished'],
        team_leader=request.json['team_leader']
    )
    session.add(job)
    session.commit()
    return jsonify({'success': 'OK'})
