import pytest
from twitteranalysis.utils.auth import AuthHandler


def test_oauthone_public():
    auth_handler = AuthHandler("OAuth1a")

    assert callable(auth_handler.api().configuration)


def test_oauthone_user_access():
    auth_handler = AuthHandler("OAuth1a", public_only=False)

    assert callable(auth_handler.api().configuration)


def test_oauthtwo_public():
    auth_handler = AuthHandler("OAuth2")

    assert callable(auth_handler.api().configuration)


def test_oauthtwo_public_implicit():
    auth_handler = AuthHandler()

    assert callable(auth_handler.api().configuration)


def test_oauthtwo_user_access():
    with pytest.raises(ValueError) as exc_info:
        AuthHandler("OAuth2", public_only=False)

    assert "Cannot access user specific API using OAuth 2" in str(exc_info)


def test_auth_invalid_type():
    with pytest.raises(TypeError) as exc_info:
        AuthHandler(3)

    assert "Expected oauth_version to be type str. Got" in str(exc_info)


def test_auth_invalid_oauth_version():
    with pytest.raises(ValueError) as exc_info:
        AuthHandler("OAuth3")

    assert "Invalid oauth_version. Expected values: 'OAuth1a' or 'OAuth2'." in str(
        exc_info)


def test_auth_invalid():
    with pytest.raises(ValueError) as exc_info:
        auth_handler = AuthHandler()
        auth_handler._auth = None  # mock a hole in logic causing _auth to be None
        auth_handler.api()

    assert "Invalid authentication provided." in str(exc_info)
