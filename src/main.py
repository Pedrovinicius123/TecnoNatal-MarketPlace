from flask import Flask, render_template, request
from flask_migrate import Migrate
from dotenv import load_dotenv
from db import db, access_database
from cripto import *

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///banco.db"
app.config['SQLALCHEMY_TRACKMODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY')

db.init_app(app)
migrate = Migrate(app, db)
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if len(request.form) > 0:
        nome = request.form['name']
        senha = request.form['password']
        is_seller = request.form['is_seller']

    return render_template('login.html')

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)
    
