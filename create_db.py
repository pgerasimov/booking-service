from app import db
from wsgi import app

with app.app_context():
    db.create_all()
