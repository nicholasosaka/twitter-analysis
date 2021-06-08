import pytest
from twitteranalysis.utils.config import AppConfig


def test_get_api_key():
    api_config = AppConfig()
    assert api_config.get_api_key() is not None


def test_get_api_secret_key():
    api_config = AppConfig()
    assert api_config.get_api_secret_key() is not None


def test_get_bearer_token():
    api_config = AppConfig()
    assert api_config.get_bearer_token() is not None


def test_get_access_token():
    api_config = AppConfig()
    assert api_config.get_access_token() is not None


def test_get_access_secret_token():
    api_config = AppConfig()
    assert api_config.get_access_secret_token() is not None
