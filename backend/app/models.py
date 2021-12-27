from app import db, login
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.String(100), primary_key=True)
    admin = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(45))
    surname = db.Column(db.String(45))
    secondname = db.Column(db.String(45))
    email = db.Column(db.String(60), unique=True)
    # certificates = db.relationship('Certificate', backref='users', lazy=False, uselist=False)
    # characteristics = db.relationship('Characteristic', backref='users', lazy=False, uselist=False)

    def get_name(self, id):
        return User.query.filter(self.id == id).first().name

class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(15), unique=True)

class Speciality(db.Model):
    __tablename__ = 'specialitys'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    code = db.Column(db.String(10), unique=True)
    name = db.Column(db.String(80), unique=True)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), unique=True)

@login.user_loader
def load_user(id):
    return User.query.get(str(id))