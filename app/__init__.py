import logging

from flask import Flask
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from flask_migrate import Migrate
from app.config import Config
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegistrationForm, SlotGenerationForm, MySlots
from app.models import db, Users
from app.slot_generation import slot_generation


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    login = LoginManager(app)

    @login.user_loader
    def load_user(id):
        return Users.query.get(int(id))

    @app.route('/')
    @app.route('/index')
    def index():
        return render_template('index.html', title='Booking service', active='index')

    @app.route('/login')
    def login():
        form = LoginForm()

        if current_user.is_authenticated:
            flash('Вы уже авторизованы')
            return redirect(url_for('schedule'))

        return render_template('login.html', form=form, title="Authorization", active='login')

    @app.route('/registration')
    def register():
        form = RegistrationForm()
        return render_template('registration.html', form=form, title="Registration", active='registration')

    @app.route('/process_login', methods=['POST'])
    def process_login():
        form = LoginForm()

        user = Users.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли')
            logging.info('Auth success')
            return redirect(url_for('schedule'))

        flash('Wrong credentionals')
        logging.error('wrong credentionals')
        return redirect(url_for('login'))

    @app.route('/process_registration', methods=['POST'])
    def process_registration():
        form = RegistrationForm()
        if form.validate_on_submit():
            user_email = form.username_reg.data
            user_pass = form.password_reg.data

            if Users.query.filter_by(email=user_email).count():
                flash('User already exist')
                logging.error('User already exist')
                return redirect(url_for('register'))

            new_user = Users(email=user_email)
            new_user.set_password(user_pass)

            db.session.add(new_user)
            db.session.commit()
            flash('Registration completed')
            return redirect(url_for('schedule'))

        flash('Password error')
        logging.error('bad password')
        return redirect('register')

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('login'))

    @app.route('/schedule')
    @login_required
    def schedule():
        form = SlotGenerationForm()
        title = 'This is a magic'
        return render_template('schedule.html', title=title, active='schedule', form=form)

    @app.route('/myslots')
    def my_slots():
        form = MySlots()
        title = 'My Slots for day'
        return render_template('myslots.html', title=title, active='myslots', form=form)

    @app.route('/slots_generate', methods=['POST'])
    def slots_generate():
        form = SlotGenerationForm()
        if form.validate_on_submit():
            slot_generation(form)
            return redirect(url_for('schedule'))

    @app.route('/get_my_slots')
    def get_my_slots():
        form = MySlots()
        if form.validate_on_submit():
            pass
    #       Берем все из базы по дате-юзеру и показываем


    return app
