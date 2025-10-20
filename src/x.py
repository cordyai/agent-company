import dotenv
import os
import tweepy

dotenv.load_dotenv(".env.local")

X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")
X_API_KEY = os.getenv("X_API_KEY")
X_API_KEY_SECRET = os.getenv("X_API_KEY_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")

# Authenticate
client = tweepy.Client(
    bearer_token=X_BEARER_TOKEN,
    consumer_key=X_API_KEY,
    consumer_secret=X_API_KEY_SECRET,
    access_token=X_ACCESS_TOKEN,
    access_token_secret=X_ACCESS_TOKEN_SECRET,
)

# timeline = client.get_home_timeline()
# for tweet in timeline.data:
#     print(f"Tweet ID: {tweet.id} | Text: {tweet.text} | Author: {tweet.author_id}")

client.create_tweet(text="Hello from automated post! #Python")

# # Post a tweet
# response = client.create_tweet(text="Hello from automated post! #Python")
# print("Tweet posted successfully!")

# auth = tweepy.OAuth1UserHandler(
#     consumer_key=X_API_KEY,
#     consumer_secret=X_API_KEY_SECRET,
#     access_token=X_ACCESS_TOKEN,
#     access_token_secret=X_ACCESS_TOKEN_SECRET,
# )

# api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
