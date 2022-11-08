import cryptography
from cryptography.fernet import Fernet
import os

name_file = input('name_file : ')
with open(name_file, 'wb') as keyfile:
    key = Fernet.generate_key()
    keyfile.write(key)
    keyfile.close()