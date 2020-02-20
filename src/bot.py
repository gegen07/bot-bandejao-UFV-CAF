import tweepy
import settings

auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_SECRET_API_KEY)
auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_SECRET_TOKEN)

api = tweepy.API(auth)

#tweet = []

#api.update_status(tweet)