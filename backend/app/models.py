from app import db, login
from datetime import datetime
from flask_login import UserMixin


users_roles = db.Table('users_roles',
    db.Column('user_id', db.String(100), db.ForeignKey('users.id')),
    db.Column(('role_id'), db.Integer, db.ForeignKey('roles.id'))
)
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(45))
    surname = db.Column(db.String(45))
    secondname = db.Column(db.String(45))
    email = db.Column(db.String(60), unique=True)
    group_id = db.Column(
        db.Integer, 
        db.ForeignKey(
            'groups.id', 
            ondelete='cascade', 
            onupdate='cascade'), 
            nullable=True)
    certificates = db.relationship('Certificate', backref='user', lazy='joined')
    characteristics = db.relationship('Characteristic', backref='user', lazy='joined')
    payments = db.relationship('Payment', backref='user', lazy='joined')

    def get_name(self, id):
        return User.query.filter(self.id == id).first().name

class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(15), unique=True)
    users = db.relationship('User', backref='groups', lazy='joined')
    speciality_id = db.Column(
                              db.Integer, 
                              db.ForeignKey(
                                  'specialitys.id', 
                                  ondelete='cascade', 
                                  onupdate='cascade'), 
                              nullable=True)


class Speciality(db.Model):
    __tablename__ = 'specialitys'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(10), unique=True)
    name = db.Column(db.String(80), unique=True)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), unique=True)
    users = db.relationship('User', secondary='users_roles',
        backref=db.backref('roles', lazy='dynamic'))

class Certificate(db.Model):    # Справки
    __tablename__ = 'certificates'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_date = db.Column(db.Date, index=True, default=datetime.utcnow)
    remove_date = db.Column(db.Date, index=True, nullable=True)
    archive = db.Column(db.Boolean, default=False)
    text = db.Column(db.String(300))
    user_id = db.Column(db.String(100), db.ForeignKey('users.id', onupdate='cascade'), nullable=False)
    status_id = db.Column(
                          db.Integer, 
                          db.ForeignKey(
                              'statuses.id', 
                              ondelete='cascade', 
                              onupdate='cascade'))

    def get_all_raws():
        return [{
            'id': r.id,
            'name': User.query.filter(User.id==r.user_id).first().name,
            'surname': User.query.filter(User.id==r.user_id).first().surname,
            'secondname': User.query.filter(User.id==r.user_id).first().secondname,
            'email': User.query.filter(User.id==r.user_id).first().email,
            'text': r.text,
            'archive': r.archive,
        } for r in Certificate.query.all()]

class Characteristic(db.Model): # Характеристики
    __tablename__ = 'characteristics'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    respondibilities = db.Column(db.String(300), nullable=True) # What doing in group
    school = db.Column(db.String(150), nullable=False)
    school_graduation = db.Column(db.String(5), nullable=False)
    MPT_entrance = db.Column(db.String(5), nullable=False)
    place = db.Column(db.String(100))
    create_date = db.Column(db.Date, index=True, default=datetime.utcnow)
    remove_date = db.Column(db.Date, index=True, nullable=True)
    archive = db.Column(db.Boolean, default=False)
    user_id = db.Column(db.String(100), db.ForeignKey('users.id', onupdate='cascade'), nullable=False)
    status_id = db.Column(
                          db.Integer, 
                          db.ForeignKey(
                              'statuses.id', 
                              ondelete='cascade', 
                              onupdate='cascade'))

    def get_all_raws():
        return [{
            'id': r.id,
            'name': User.query.filter(User.id==r.user_id).first().name,
            'surname': User.query.filter(User.id==r.user_id).first().surname,
            'secondname': User.query.filter(User.id==r.user_id).first().secondname,
            'email': User.query.filter(User.id==r.user_id).first().email,
            'archive': r.archive,
        } for r in Characteristic.query.all()]

class Status(db.Model):
    __tablename__ = 'statuses'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    certificates = db.relationship('Certificate', backref='statuses', lazy='joined')
    characteristics = db.relationship('Characteristic', backref='statuses', lazy='joined')

class Payment(db.Model):    # Платёжки
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    payment = db.Column(db.String(300), nullable=False)
    semestr = db.Column(db.String(45), nullable=False)
    create_date = db.Column(db.Date, index=True, default=datetime.utcnow)
    user_id = db.Column(db.String(100), db.ForeignKey('users.id', onupdate='cascade'), nullable=False)

@login.user_loader
def load_user(id):
    return User.query.get(str(id))