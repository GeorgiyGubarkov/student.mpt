from datetime import datetime
from app import app, db
from app.models import Certificate, User
from config import Config
from flask import redirect, request, jsonify, url_for
from flask_login import current_user, login_user, logout_user

@app.route('/')
def index():
    return 'Simple application'

@app.route('/certificate', methods=['GET', 'POST'])
def certificate():
    current_user = User.query.filter(User.id=='123').first()
    current_user.admin = False
    if request.method == 'GET':
        if current_user.admin is False:
            return jsonify({
                'name': current_user.name,
                'surname': current_user.surname,
                'secondname': current_user.secondname,
                'email': current_user.email,
            })
        certificates = Certificate.get_all_raws()
        return jsonify(certificates)
    formData = jsonify(request.form).get_json()
    db.session.add(Certificate(
        text = formData['ticket'],
        user_id = current_user.id,
    ))
    db.session.commit()
    return 'Your ticket is apply. Check status in personal area'

@app.route('/certificate/<int:id>', methods=['DELETE', 'PUT'])
def remove_update_certificate(id):
    current_user = User.query.filter(User.id=='123').first()
    certificate = Certificate.query.filter(id==Certificate.id).first()
    if current_user.admin == False:
        return redirect(url_for('index'))
    if certificate is None:
        return 'Bad Gateway'
    if request.method == 'PUT':
        certificate.archive = True
        certificate.remove_date = datetime.utcnow()
        db.session.commit()
        return 'Seccess'
    formData = jsonify(request.form).get_json()
    # Вызвать функцию для отправки на почту уведомления об отказе и причину
    certificate.delete()
    return formData['reason']


