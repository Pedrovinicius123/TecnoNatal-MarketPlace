from cryptography.fernet import Fernet
import os

def encrypt_database():
    key = Fernet.generate_key()
    fernet = Fernet(key)

    with open(os.path.join('instance', 'banco.db'), 'rb') as file:
        data = file.read()
    
    crypto_data = fernet.encrypt(data)

    with open(os.path.join('instance', 'banco.db'), 'wb') as encrypted_file:
        encrypted_file.write(crypto_data)

    os.environ['IS_ENCRYPTED'] = 'true'
    os.environ['KEY_DATABASE'] = key.decode()

def decrypt_database():
    if os.getenv('IS_ENCRYPTED') == 'true':
        key = os.getenv('KEY_DATABASE').encode()
        fernet = Fernet(key)
        decrypted_data = None

        with open(os.path.join('instance','banco.db'), 'rb') as encrypted_file:
            decrypted_data = fernet.decrypt(encrypted_file.read())

        with open(os.path.join('instance', 'banco.db'), 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
