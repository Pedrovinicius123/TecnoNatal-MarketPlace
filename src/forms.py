from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('Email/Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enter')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    options = RadioField('User type', validators=[DataRequired()], choices=[(True, 'Seller'), (False, 'Common')])
    password = PasswordField('Password', validators=[DataRequired()])
    rep_password = PasswordField('Repeat Password', validators=[DataRequired()])
    submit = SubmitField("Enter")
