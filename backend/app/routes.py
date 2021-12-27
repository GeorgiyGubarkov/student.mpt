from app import app, db
from config import Config

@app.route('/')
def index():
    return 'Simple application'