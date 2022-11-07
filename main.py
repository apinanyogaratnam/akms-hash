import hashlib
import os


def hash_api_key(api_key: str) -> str:
    salt = os.urandom(32)
    key = hashlib.pbkdf2_hmac("sha256", api_key.encode("utf-8"), salt, 100000)

    storage = salt + key

    return storage


def get_salt_from_storage(storage: str) -> str:
    return storage[:32]


def get_hashed_api_key_from_storage(storage: str) -> str:
    return storage[32:]


def verify_key(storage: str, api_key: str) -> bool:
    salt = get_salt_from_storage(storage)
    hashed_api_key = get_hashed_api_key_from_storage(storage)

    received_hashed_api_key = hashlib.pbkdf2_hmac("sha256", api_key.encode("utf-8"), salt, 100000)

    return hashed_api_key == received_hashed_api_key
