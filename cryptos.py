from cryptography.fernet import Fernet
import cryptography
import ast

key_name = "secret.key"
psswd_name = "psswd.aab"

data = {}

def generate_key():
    with open(key_name, "wb") as key_file:
        key_file.write(Fernet.generate_key())

def load_key():
    try:
        return open(key_name, "rb").read()
    except FileNotFoundError:
        return False


def encrypt_message(message):
    f = Fernet(load_key())
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    f = Fernet(load_key())
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

def load_password_file():
    try:
        with open(psswd_name, "rb") as z:
            d_data = decrypt_message(z.read())
            _data = eval(d_data)
            return _data
    except (TypeError, cryptography.fernet.InvalidToken):
        return "Missing or invalid key"

def update_password_file():
    with open(psswd_name, "ab") as passwords:
        passwords.truncate(0)
        passwords.write(encrypt_message(str(data)))
    

def input_info():
    x1 = input()
    x2 = input()
    data.update({x1: x2})
    if load_key() != False:
        update_password_file()

try:
    open(psswd_name)
    data = load_password_file()
except FileNotFoundError:
    open(psswd_name, "xb")
    generate_key()


while True:
    x = input()
    if x=="1":
        input_info()
    elif x=="2":
        print(load_password_file()) 
    
        
            

#Token to rzecz, którą zamierzamy zaszyfrować
#InvalidToken wypierdala jak token w jakiś sposób jest niepoprawny (niezamieniony na binarny, itd.)
#Narazie działa to spoko
#Tylko trzeba jeszcze popracować nad wykrywaniem czy istnieje już jakaś psswd.aab czy nie (w ładniejszy sposób)
#i jakieś GUI w konsolce
#ale to potem XD
