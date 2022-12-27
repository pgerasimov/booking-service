from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, DateTimeField, SelectField, \
    IntegerField
from wtforms.validators import DataRequired, Regexp, EqualTo, NumberRange

regexp = r'(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z\S+]{8,}'


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()], render_kw={
        "class": "form-control",
        "placeholder": "Enter email",
        "type": "email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={
        "class": "form-control",
        "placeholder": "Enter Password",
        "type": "password"})
    remember_me = BooleanField('Remember Me', default=True,
                               render_kw={"class": "form-check-input"})
    submit = SubmitField('Log In', render_kw={
        "class": "btn btn-primary",
        "Type": "submit"})


class RegistrationForm(FlaskForm):
    username_reg = StringField(
        'Email',
        validators=[DataRequired()],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter email",
            "type": "email"})
    password_reg = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Regexp(regexp)
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter Password",
            "type": "password"})
    password_reg_confirm = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Regexp(regexp),
            EqualTo('password_reg')
        ],
        render_kw={
            "class": "form-control",
            "placeholder": "Enter Password",
            "type": "password"})
    submit_reg = SubmitField(
        'Зарегистрироваться',
        render_kw={
            "class": "btn btn-primary",
            "Type": "submit"})


class SlotGenerationForm(FlaskForm):
    work_date = DateField('Date', validators=[DataRequired()])
    start_time = IntegerField('Start time', validators=[NumberRange(min=8, max=20)], render_kw={"placeholder": "8"})
    end_time = IntegerField('End time', validators=[NumberRange(min=9, max=21)], render_kw={"placeholder": "21"})
    duration = SelectField('Длительность приема', choices=[('1', '1 Час'), ('2', '2 Часа')])
    submit = SubmitField(
        'Сгенерировать',
        render_kw={
            "class": "btn btn-primary",
            "Type": "submit"})


class MySlots(FlaskForm):
    date = DateField('Date', validators=[DataRequired()])
    submit = SubmitField(
        'Показать',
        render_kw={
            "class": "btn btn-primary",
            "Type": "submit"})
