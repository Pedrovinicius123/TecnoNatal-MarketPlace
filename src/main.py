from flask import Flask, render_template, request, session, url_for, redirect
from flask_login import login_required, logout_user
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash

from forms import LoginForm, RegisterForm
from models import User, Product
from users import bp_users, bp_products
from dotenv import load_dotenv
from db import db

import os, inspect

load_dotenv()

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///banco.db"
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')

app.register_blueprint(bp_users, url_prefix='/users')
app.register_blueprint(bp_products, url_prefix='/products')

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/', methods=['GET', 'POST'])
def index():
    user = request.args.get('u')
    email = request.args.get('e')
    return render_template('index.html', user=user, email=email)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html')

@app.route('/logout', methods=['POST'])
@login_required
def logout():
    if request.method == 'POST':
        session.clear()
        logout_user()

        return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        nome_email = login_form.email.data
        password = login_form.password.data
        user = User.query.filter_by(name=nome_email).first()
        user_iter = next((u for u in inspect.getmembers(user) if not u.startswith('__')), None)

        if not user or not user.verify_password(password):
            email = User.query.filter_by(email=nome_email).first()

            if not email or not email.verify_password(password):
                return redirect(url_for('login', err='User not found/Incorrect password'))
            return redirect(url_for('', user=User.query.filter_by(email=nome_email).first().name, email=email))
        return redirect(url_for('', user=user, email=User.query.filter_by(email=nome_email).first().email))

    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    load_dotenv()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
