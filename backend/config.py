class Config():
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://student:User@localhost/student'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    DEBUG = True
    SECRET_KEY = 'anyanyanyanyanyanyanyanyanyanyanyanyanyanyanyanyanyanyany'

    scopes = ['https://www.googleapis.com/auth/userinfo.email',
              'https://www.googleapis.com/auth/userinfo.profile',
              'openid']

    token_url = "https://www.googleapis.com/oauth2/v4/token"
    user_info_url = 'https://www.googleapis.com/oauth2/v2/userinfo'
    redirect_uri = 'http://localhost:5000'

    oauth = {"web":
    {
    "client_id":"638853405772-clt83ikf51ac65ajn244ou1sbkf67tdf.apps.googleusercontent.com",
    "project_id":"test-332117",
    "auth_uri":"https://accounts.google.com/o/oauth2/auth",
    "token_uri":"https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
    "client_secret":"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",
    "redirect_uris":["http://mysite.com:8000/social-auth/complete/google-oauth2/"]
    }
}
