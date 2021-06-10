from twitteranalysis.utils.config import AppConfig
import tweepy


class AuthHandler:
    """Handles authentication into Twitter API.

    Parameters
    ----------
    oauth_version : str
        OAuth version to use.
        Note: OAuth2 provides only public API access.

    public_only : bool
        When false, requires access token (with secret) and allows for API access that is user specific.
        When true, API access is to only public resources.
    """

    def __init__(self, oauth_version="OAuth2", public_only=True):
        ac = AppConfig()
        self._auth = None

        if type(oauth_version) is not str:
            raise TypeError(
                "Expected oauth_version to be type str. Got {0}.".format(type(oauth_version)))

        if oauth_version == "OAuth2":
            self._auth = tweepy.AppAuthHandler(
                ac.get_api_key(), ac.get_api_secret_key())

        elif oauth_version == "OAuth1a":
            self._auth = tweepy.OAuthHandler(
                ac.get_api_key(), ac.get_api_secret_key())
        else:
            raise ValueError(
                "Invalid oauth_version. Expected values: 'OAuth1a' or 'OAuth2'.")

        if public_only == False:
            if oauth_version == "OAuth2":
                raise ValueError(
                    "Cannot access user specific API using OAuth 2")
            self._auth.set_access_token(
                ac.get_access_token(), ac.get_access_secret_token())

    def api(self):
        """Returns Tweepy's Twitter API wrapper
        """
        if self._auth is not None:
            return tweepy.API(self._auth)
        else:
            raise ValueError("Invalid authentication provided.")
