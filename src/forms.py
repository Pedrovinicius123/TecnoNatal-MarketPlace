from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField('Nome', validators)
