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

class Certificate(db.Model):    # Справки
    __tablename__ = 'certificates'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    create_date = db.Column(db.Date, index=True, default=datetime.utcnow)
    remove_date = db.Column(db.Date, index=True, nullable=True)
    archive = db.Column(db.Boolean, default=False)
    text = db.Column(db.String(300))

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

class Payment(db.Model):    # Платёжки
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    payment = db.Column(db.String(300), nullable=False)
    semestr = db.Column(db.String(45), nullable=False)
    create_date = db.Column(db.Date, index=True, default=datetime.utcnow)

@login.user_loader
def load_user(id):
    return User.query.get(str(id))