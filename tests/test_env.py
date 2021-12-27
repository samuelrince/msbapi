import os


def test_env():
    assert os.getenv('CLIENT_URL') is not None
    assert os.getenv('BASE_PATH') is not None
    assert os.getenv('AUTH_TOKEN') is not None
