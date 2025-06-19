from db import db
from werkzeug.security import check_password_hash
from flask_login import UserMixin
import re

def is_password_strong(password):
    return len(password) >= 8 and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password)

class User(db.Model, UserMixin):
    __tablename__ = "user"

    # Chave primária
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Atributo monovalorado
    name = db.Column(db.String(300), nullable=False, unique=True)

    # Atributos monovalorados
    email = db.Column(db.String(300), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))

    # É vendedor
    is_seller = db.Column(db.Boolean, nullable=False, default=False)
    prods = []
    
    @property
    def products(self):
        raise ArithmeticError('Product not defined')

    @products.getter
    def products(self):
        return self.prods

    def add_product(self, other):
        self.prods.append(other)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    

class Product:
    id = 0
    products = []
    def __init__(self, seller, name, description, price):
        self.seller = seller
        self.name = name
        self.description = description
        self.price = price

        Product.id += 1
        Product.products.append(self)
