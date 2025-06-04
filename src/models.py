from db import db
from werkzeug.security import generate_password_hash, check_password_hash
import re

def is_password_strong(password):
    return len(password) >= 8 and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password)

class User(db.Model):
    __tablename__ = "usuario"

    # Chave primária
    id = db.Column(db.Integer, primary_key=True)

    # Atributo monovalorado
    name = db.Column(db.String(300), nullable=False, unique=True)

    # Atributos monovalorados
    email = db.Column(db.String(300), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))

    # É vendedor
    is_seller = db.Column(db.Boolean, nullable=False, unique=True)

    # Número de vendas
    n_sales = db.Column(db.Integer(1000))

    @property
    def password(self):
        raise ArithmeticError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    

class Product(db.Model):
    __tablename__ = "produto"

    # Chave primária
    id = db.Column(db.Integer, primary_key=True)

    # Nome do produto
    name = db.Column(db.String(40))

    # Descrição
    description = db.Column(db.String(300))

    # Vendedor e preços
    seller = db.Collumn(db.String(100), db.ForeignKey('user.id'), nullable=False, unique=True)

    @property
    def price(self):
        raise AttributeError('Price can not be read directly')

    @price.setter
    def price(self, new_price):
        self.price = new_price

    @price.getter
    def get_price(self):
        return self.price
