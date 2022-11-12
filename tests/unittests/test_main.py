from akms_hash.main import hash_api_key, verify_api_key


def test_hash_api_key():
    api_key = 'test'
    hashed_api_key = hash_api_key(api_key)
    assert isinstance(hashed_api_key, bytes)


def test_verify_api_key():
    api_key = 'test'
    hashed_api_key = hash_api_key(api_key)

    expected = True
    actual = verify_api_key(hashed_api_key, api_key)
    assert actual == expected

    expected = False
    actual = verify_api_key(hashed_api_key, 'test1')
    assert actual == expected
