from flask.blueprints import Blueprint
from flask import render_template

bp_users = Blueprint("users", __name__, template_folder='templates')
bp_products = Blueprint("products", __name__, template_folder='templates')

@bp_users.route('/register')
def create_user():
    return render_template('register.html')

@bp_products.route('/new')
def create_product():
    return render_template('assign_product.html')