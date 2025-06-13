from db import db
from werkzeug.security import check_password_hash
import re

def is_password_strong(password):
    return len(password) >= 8 and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) and re.search(r'[0-9]', password)

class User(db.Model):
    __tablename__ = "user"

    # Chave primária
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Atributo monovalorado
    name = db.Column(db.String(300), nullable=False, unique=True)

    # Atributos monovalorados
    email = db.Column(db.String(300), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))

    # Número de vendas
    n_sales = db.Column(db.Integer())

    @property
    def is_seller(self):        
        raise ArithmeticError('Is_seller is not defined')

    @is_seller.setter
    def is_seller(self, other):
        self.__is_seller_attr = other

    @is_seller.getter
    def is_seller(self):
        return self.__is_seller_attr

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
    seller = db.Column(db.String(100), db.ForeignKey('user.id'), nullable=False, unique=True)

    @property
    def price(self):
        raise AttributeError('Price can not be read directly')

    @price.setter
    def price(self, new_price):
        self.price = new_price

    @price.getter
    def get_price(self):
        return self.price
