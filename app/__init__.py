from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from app.config import Config
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegistrationForm
from app.models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    login = LoginManager(app)

    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html', title='Booking service')

    @app.route('/login')
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            print(form.email.data)
        return render_template('login.html', form=form, title="Authorization")

    @app.route('/register')
    def register():
        form = RegistrationForm()
        return render_template('registration.html', form=form, title="Registration")

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        return 'ok'

    return app