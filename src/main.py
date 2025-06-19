from flask import Flask, render_template, request, session, url_for, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash

from forms import LoginForm
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

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db.init_app(app)
migrate = Migrate(app, db)

@login_manager.user_loader
def load_user(user_id):
    # Esta função deve receber apenas o user_id e retornar o usuário correspondente
    return User.query.get(int(user_id))

@app.route('/', methods=['GET', 'POST'])
def index():
    username = request.args.get('user')
    email = request.args.get('email')

    if not username or email:
        id = session.get('user_id')
        if id:
            user = User.query.get(id)
            if user:           
                username = user.name
                email = user.email

    return render_template('index.html', user=username, email=email, products=Product.products)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = load_user(session['user_id'])
    return render_template('profile.html', user=user)

@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    session.clear()
    

    return redirect(url_for('index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        nome_email = login_form.email.data
        password = login_form.password.data
        user = User.query.filter_by(name=nome_email).first()
        #user_iter = next((u for u in inspect.getmembers(user) if not u.startswith('__')), None)

        if not user or not user.verify_password(password):
            email = User.query.filter_by(email=nome_email).first()

            if not email or not email.verify_password(password):
                return redirect(url_for('login', err='User not found/Incorrect password'))

            login_user(email)
            return redirect(url_for('index', user=nome_email, email=email.email))

        login_user(user)
        session['user_id'] = user.id
        return redirect(url_for('index', user=nome_email, email=user.email))

    return render_template('login.html', form=login_form)

if __name__ == '__main__':
    load_dotenv()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    
