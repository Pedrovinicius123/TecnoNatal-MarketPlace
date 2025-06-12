from flask_wtf import FlaskForm, StringField, PasswordField, SubmitField
from flask_wtf.validators import DataRequired, Email, Lenght
import re

class LoginForm(FlaskForm):
    email = StringField('Email/Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Lenght(min=8, max=15)])
    submit = SubmitField('Enter')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Lenght(min=8, max=15)])
    rep_password = PasswordField('Repeat Password', validators=[DataRequired(), Lenght(min=8, max=15)])
