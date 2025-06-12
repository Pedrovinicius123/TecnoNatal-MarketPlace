from flask import Flask, render_template, request, session, url_for, redirect
from flask_login import login_required, logout_user
from flask_migrate import Migrate

from forms import LoginForm, RegisterForm
from models import User, Product
from users import bp_users, bp_products
from dotenv import load_dotenv
from db import db

import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///banco.db"
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')
app.register_blueprint(bp_users, url_prefix='/users')
app.register_blueprint(bp_products, url_prefix='/products')

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
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
    if request.method == 'POST':
        session['user'] = request.form['name']

        user = User.query.filter_by(email=request.form['name'], password=request.form['password']).first()
        if not any(user):
            email = User.query.filter_by(email=request.form['name'], password=request.form['password']).first()
            if not any(email):
                return redirect(url_for('login'))
            return redirect(url_for('index', user=User.query.filter_by(email=request.form['name']).first().name, email=email))
        return redirect(url_for('index', user=user, email=User.query.filter_by(email=name.form['name']).first().email))

    return render_template('login.html')

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)
    
