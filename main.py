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


def verify_key(storage: str, api_key: str) -> bool:
    salt = get_salt_from_storage(storage)
    key = get_key_from_storage(storage)

    new_key = hashlib.pbkdf2_hmac('sha256', api_key.encode('utf-8'), salt, 100000)

    if key == new_key:
	return True

    return False
