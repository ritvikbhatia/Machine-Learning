import tweepy
from textblob import TextBlob
oauth_token 		= "1423359655-KJoeQIpfeC3EWICNP6QjA708vJ6KcIZiCTjEmhs"
oauth_token_secret	= "G0rV0N6RqvRAQaa3q9lQZ0C1XDAGZMEKwdQEqvrsEY16o"

consumer_key 		= "pvrfGmCiVcz7MkQAH0TKwSc8R"
consumer_secret 	= "djGNRGujm9HvqKT9cuuuTVBf5D6nngYVzuCsqceZt0qbwLDFd0"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(oauth_token,oauth_token_secret)

api=tweepy.API(auth)
public_tweets=tweepy.Cursor(api.search,q='race 3',lang='English').items(100)
for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
