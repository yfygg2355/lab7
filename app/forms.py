from flask_wtf import FlaskForm
from wtforms import BooleanField, EmailField, IntegerField, StringField, PasswordField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Length, NumberRange, Email, EqualTo, Regexp

from app.models import User

class ChangePasswordForm(FlaskForm):
    current_password = PasswordField(label='Current Password', validators=[DataRequired(message="This field is required."), Length(min=4, max=10, message='The password must be between 4 and 10 characters.')])
    new_password = PasswordField(label='New Password', validators=[DataRequired(message="This field is required."), Length(min=4, max=10, message='The password must be between 4 and 10 characters.')])
    confirm_password = PasswordField(label='Confirm New Password', validators=[DataRequired(message="This field is required."), Length(min=4, max=10, message='The password must be between 4 and 10 characters.')])
    submit = SubmitField("Change Password")

class TodoForm(FlaskForm):
    title = StringField("Enter a task here", validators=[DataRequired(message="This field is required.")])
    description = StringField("Describe your task", validators=[DataRequired(message="This field is required.")])
    submit = SubmitField("Save")

class FeedbackForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired(message="This field is required.")])
    text = TextAreaField(label='Write your review here', validators=[DataRequired(message="Це поле є обов'язковим.")])
    rating = IntegerField(label='Rate it from 1 to 5', validators=[DataRequired(message="Це поле є обов'язковим."), NumberRange(min=1, max=5, message="Від 1 до 5.")])
    submit = SubmitField('Submit')

class RegistrationForm(FlaskForm):
    username = StringField('Імя', validators=[
        DataRequired(message="Це поле є обов'язковим."),
        Length(min=4, max=14, message='Імя користувача має містити від 4 до 14 символів.'),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Імя користувача має містити лише літери, цифри, крапки або підкреслення.')
    ])
    email = EmailField('Email', validators=[
        DataRequired(message="Це поле є обов'язковим."),
        Email(message="Неправильний email.")
    ])
    password = PasswordField('Пароль', validators=[
        DataRequired(message="Це поле є обов'язковим."),
        Length(min=6, message='Password must be more than 6 characters long')
    ])
    confirm_password = PasswordField('Повторіть пароль', validators=[
        DataRequired(message="Це поле є обов'язковим."),
        EqualTo('password', message='Passwords must match.')
    ])
    submit = SubmitField('Sign up')

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user:
            raise ValidationError('Username already exists. Choose a different one.')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user:
            raise ValidationError('Email already exists. Please use a different one.')

class LoginForm(FlaskForm):
    email = StringField(label='Еmail', validators=[DataRequired(message="Це поле є обов'язковим.")])
    password = PasswordField(label='Пароль', validators=[DataRequired(message="Це поле є обов'язковим."), Length(min=4, max=10, message='The password must be between 4 and 10 characters.')])
    remember = BooleanField(label='Remember me')
    submit = SubmitField("Sign In")