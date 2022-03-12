class Config():
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:User@localhost/student'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = 'anyanyanyanyanyanyanyanyanyanyanyanyanyanyanyanyanyanyany'
