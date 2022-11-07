import os
import hashlib


def hash_api_key(api_key: str) -> str:
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac('sha256', api_key.encode('utf-8'), salt, 100000)
    
    storage = salt + key

    return storage


def get_salt_from_storage(hashed_key: str) -> str:
    return hashed_key[:32]


def get_key_from_storage(hashed_key: str) -> str:
    return hashed_key[32:]
