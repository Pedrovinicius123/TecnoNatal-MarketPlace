from flask_sqlalchemy import SQLAlchemy
from cripto import *
import os

db = SQLAlchemy()

def access_database(app, db):
    key_is_generated = os.getenv('KEY_IS_GENERATED')
    is_encrypted = os.getenv('IS_ENCRYPTED')

    with app.app_context():
        db.create_all()

        if not key_is_generated == 'true':
            encrypt_database()
            os.environ['IS_ENCRYPTED'] = 'true'

        if is_encrypted == 'true':
            decrypt_database()
            return db        
        