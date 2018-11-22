import hashlib
import time
import uuid


def generate_password(password):
    sha = hashlib.sha512()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()

def genarator_token():
    token = str(uuid.uuid3(uuid.uuid4(), str(time.time())))
    return token
