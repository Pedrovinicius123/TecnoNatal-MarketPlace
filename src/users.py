from flask import Blueprints, render_template

bp_users = Blueprints("users", __name__, template_folder='templates')
bp_products = Blueprints("products", __name__, template_folder='templates')

@bp_users.route('/create')
def create_user():
    return render_template('login.html')

@bp_products.route('/product/new')
def create_product():
    return render_template('assign_product.html')