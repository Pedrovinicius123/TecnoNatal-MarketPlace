from flask.blueprints import Blueprint
from flask import render_template, redirect, url_for, session
from models import User
from forms import RegisterForm

from db import db

bp_users = Blueprint("users", __name__, template_folder='templates')
bp_products = Blueprint("products", __name__, template_folder='templates')

@bp_users.route('/register', methods=['GET', 'POST'])
def create_user():
    reg_form = RegisterForm()
    if reg_form.is_submitted():
        username = reg_form.username.data
        email = reg_form.email.data
        option = reg_form.options.data
        password = reg_form.password.data
        repeat_password = reg_form.rep_password.data

        if password != repeat_password:
            return redirect(url_for('register', err="Passwords don't match"))
        
        print(username, password)

        user = User(name=username, email=email, is_seller=option)
        user.password = password

        db.session.add(user)
        db.session.commit()

        

        return render_template('index.html', user=username, email=email)

    return render_template('register.html', form=reg_form)

@bp_products.route('/new')
def create_product():
    return render_template('assign_product.html')