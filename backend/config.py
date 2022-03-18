class Config():
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://root:12345@dbPostgres:5432/student'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = 'anyanyanyanyanyanyanyanyanyanyanyanyanyanyanyanyanyanyany'
