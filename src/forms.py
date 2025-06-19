from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField
from wtforms.validators import DataRequired, Email, ValidationError
from wtforms.widgets import TextArea

def maximum_price(form, field):
    if float(field.data) > 1000:
        raise ValidationError('You are not Nintendo (c) ...')


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

class CreateProductForm(FlaskForm):
    product_name = StringField('Name', validators=[DataRequired()])
    product_price = StringField('Price', validators=[maximum_price])
    product_text_desc = StringField('Description', validators=[DataRequired()], widget=TextArea())
    product_tags = StringField('Tags')
    submit = SubmitField()
