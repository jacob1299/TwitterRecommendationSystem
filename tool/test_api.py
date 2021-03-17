import tweepy

consumer_key = 'dtuyCjWcmlVU2VvRiPBpgPjNv'
consumer_secret = 'ChjcQ4eqBYfM9bPzFMcYCcO5PgTc7VaU7zCtprCF3YTaqqoY4z'
access_token = '4692990596-6kDqE1WiHv0iwnkhYsiVrRX5dKJEoy8NnZUsCb7'
access_token_secret = 'wAiMryVITG4mTXuQig8LjMCoGGAflL0P6oJk6TAhFjpaU'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)