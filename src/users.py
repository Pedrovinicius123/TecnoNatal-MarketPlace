from flask.blueprints import Blueprint
from flask import render_template, redirect, url_for
from werkzeug.security import generate_password_hash
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
        
        print(username, email, password)

        users = User.query.filter_by(name=username).first()
        users_email = User.query.filter_by(email=email).first()
        print(users, users_email)

        if users is not None and users_email is not None:
            err = "User already exists"
            return redirect(url_for('users.create_user', err=err))

        user = User(name=username, email=email, password_hash=generate_password_hash(password), n_sales=0)
        user.is_seller = option

        db.session.add(user)
        db.session.commit()        

        return redirect(url_for('index', u=username, e=email))

    return render_template('register.html', form=reg_form)

@bp_products.route('/new')
def create_product():
    return render_template('assign_product.html')