import tweepy
import configparser

# Create a ConfigParser object
config = configparser.RawConfigParser()

# Read the INI file
config.read("config.ini")

# Access values from the sections
twitter_api_section = config["TwitterAPI"]
# Get keys
bearer_token = twitter_api_section["bearer_token"]
access_token = twitter_api_section["access_token"]
access_token_secret = twitter_api_section["access_token_secret"]
client_id = twitter_api_section["client_id"]
client_secret = twitter_api_section["client_secret"]

