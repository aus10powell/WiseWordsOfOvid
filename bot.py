
import tweepy
import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the INI file
config.read('config.ini')

# Access values from the INI file
username = config.get('Settings', 'username')
password = config.get('Settings', 'password')

server_host = config.get('Server', 'host')
server_port = config.getint('Server', 'port')  # Use getint to retrieve integer values


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

# Example: Post a tweet
api.update_status("Hello, world!")

# Example: Follow a user
api.create_friendship("username")

# Example: Reply to a mention
for mention in api.mentions_timeline():
    if mention.text.startswith("@your_username"):
        reply = "@{} Thanks for the mention!".format(mention.user.screen_name)
        api.update_status(reply, mention.id)
