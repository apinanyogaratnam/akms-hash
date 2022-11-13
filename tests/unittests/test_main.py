from akms_hash.main import hash_api_key, verify_api_key


def test_hash_api_key():
    api_key = 'test'
    salt = 'test'
    hashed_api_key = hash_api_key(api_key, salt)
    assert isinstance(hashed_api_key, str)
    assert len(hashed_api_key) == 64


def test_verify_api_key():
    api_key = 'test'
    salt = 'test'
    hashed_api_key = hash_api_key(api_key, salt)
    print('hashed_api_key: ', hashed_api_key)
    expected = True
    actual = verify_api_key(api_key, hashed_api_key, salt)
    print('actual: ', actual)
    assert actual == expected

    api_key = 'test1'
    expected = False
    actual = verify_api_key(api_key, hashed_api_key, salt)
    assert actual == expected
