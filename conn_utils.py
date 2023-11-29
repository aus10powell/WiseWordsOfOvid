import tweepy
import configparser

class TwitterAPIConnector:
    def __init__(self, file_path: str = "config.ini"):
        """
        Initialize the TwitterAPIConnector with the path to the INI file.

        Args:
            file_path (str, optional): Path to the INI file. Defaults to "config.ini".
        """
        self.file_path = file_path
        self.config = configparser.RawConfigParser()
        self.config.read(self.file_path)
        self.twitter_api_section = self.config["TwitterAPI"]

    def get_twitter_conn_v1(self) -> tweepy.API:
        """
        Get Twitter connection using OAuth 1.0.

        Returns:
            tweepy.API: Twitter API connection object.
        """
        auth = tweepy.OAuth1UserHandler(
            self.twitter_api_section["api_key"],
            self.twitter_api_section["api_secret"],
        )
        auth.set_access_token(
            self.twitter_api_section["access_token"],
            self.twitter_api_section["access_token_secret"],
        )
        return tweepy.API(auth)

    def get_twitter_conn_v2(self) -> tweepy.Client:
        """
        Get Twitter connection using OAuth 2.0.

        Returns:
            tweepy.Client: Twitter Client connection object.
        """
        client = tweepy.Client(
            consumer_key=self.twitter_api_section["api_key"],
            consumer_secret=self.twitter_api_section["api_secret"],
            access_token=self.twitter_api_section["access_token"],
            access_token_secret=self.twitter_api_section["access_token_secret"],
        )
        return client

    def read_twitter_config(self) -> dict:
        """
        Read Twitter API configuration from an INI file.

        Returns:
            dict: Dictionary containing Twitter API configuration values.
        """
        config_values = {
            "bearer_token": self.twitter_api_section["bearer_token"],
            "access_token": self.twitter_api_section["access_token"],
            "access_token_secret": self.twitter_api_section["access_token_secret"],
            "api_key": self.twitter_api_section["api_key"],
            "api_secret": self.twitter_api_section["api_secret"],
        }
        return config_values
