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

    # Проверьте, что запрос содержит данные в формате json,
    # а также, что данный json содержит все требуемые поля данных
    # При необходимости верните сообщение об ошибке в нужном формате

    session = db_session.create_session()

    # Если работа с таким идентификатором уже существует в базе данных,
    # верните сообщение об ошибке в нужном формате

    job = Jobs(
        id=request.json['id'],
        ...  # Проинициализируйте оставшиеся поля
    )

    # Сохраните объект job в базе данных

    return jsonify(...)  # Верните сообщение об успехе
