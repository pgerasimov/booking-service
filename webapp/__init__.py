from flask import Flask, render_template, redirect, url_for, flash
from flask_login import logout_user
from webapp.forms import LoginForm, RegistrationForm
from webapp.model import db, Users


def create_app():
    app = Flask(__name__)
    app.run(debug=True)
    app.config.from_pyfile('config.py')
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    db.init_app(app)

    @app.route("/")
    def index():
        return render_template('base.html', active='index')

    @app.route("/login")
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        return render_template(
            'login.html',
            page_title=title,
            form=login_form,
            active='login')

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()

        user = Users.query.filter_by(email=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли на сайт')
            return redirect(url_for('search'))

        else:
            flash('Неправильное имя пользователя или пароль')
            logging.error('Неправильное имя пользователя или пароль')
            return redirect(url_for('index'))
        return 'test for digitalocean'

    @app.route('/registration')
    def registration():
        # if current_user.is_authenticated:
        #     flash('Вы уже авторизованы')
        #     return redirect(url_for('search'))

        title = "Регистрация"
        registration_form = RegistrationForm()
        return render_template(
            'registration.html',
            page_title=title,
            form=registration_form,
            active='registration'
        )

    @app.route('/process_registration', methods=['POST'])
    def process_registration():

        form = RegistrationForm()

        if form.validate_on_submit():

            username = form.username_reg.data
            password = form.password_reg.data

            if Users.query.filter(Users.email == username).count():
                flash('Такой пользователь уже есть')
                logging.error('Такой пользователь уже есть')
                return redirect(url_for('registration'))

            new_user = Users(email=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()

            flash('Вы успешно зарегистрировались')
            return redirect(url_for('index'))

        flash('Пароль не удовлетворяет требованиям. Повторите ввод')

        return redirect(url_for('registration'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешно вышли из системы')
        return redirect(url_for('index'))

    return app
