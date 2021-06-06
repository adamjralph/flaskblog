from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.fields.core import BooleanField
from wtforms.validators import DataRequired, EqualTo, Length, Email


class RegistrationForm(FlaskForm):
    uername = StringField('Username',
                    validators=[DataRequired(),
                    Length(min=2, max=20)])
    email = StringField('Email',
                    validators=[DataRequired(), Email()]) 
    password = PasswordField('Password', validators=[DataRequired()])
    password = PasswordField('Confirm Password',
                    validators=[DataRequired(),
                    EqualTo('password')])
    submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                    validators=[DataRequired(), Email()]) 
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')