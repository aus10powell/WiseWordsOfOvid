import tweepy
import configparser

# Custom
from conn_utils import TwitterAPIConnector

def main():
    # Assuming you have already created an instance of TwitterAPIConnector
    twitter_connector = TwitterAPIConnector()

    # Get Twitter connection using OAuth 1.0
    api_v1 = twitter_connector.get_twitter_conn_v1()

    # Get Twitter connection using OAuth 2.0
    api_v2 = twitter_connector.get_twitter_conn_v2()

    # Test tweet
    

if __name__ == '__main__':
    main()
