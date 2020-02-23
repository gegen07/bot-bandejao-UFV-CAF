import tweepy
import settings
from spider import Read_data, Search_file
from datetime import datetime
from settings import SCHEDULE_BREAKFAST, SCHEDULE_LUNCH, SCHEDULE_DINER

auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_SECRET_API_KEY)
auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_SECRET_TOKEN)

api = tweepy.API(auth)

def _get_meals_of_day(data, time):
  meals_of_day = data[datetime.today().strftime('%A')]
  if time == SCHEDULE_BREAKFAST:
    return "Café da Manhã", meals_of_day["Café da Manhã"]
  elif time == SCHEDULE_LUNCH:
    return "Almoço", meals_of_day["Almoço"]
  elif time == SCHEDULE_DINER:
    return "Jantar", meals_of_day["Jantar"]

def PostTweet(time):
  tweet = ""

  data = Read_data(Search_file())

  meal, menu = _get_meals_of_day(data, time)
  tweet += "Cardápio - " + datetime.today().strftime('%d/%m/%Y') + " - " + meal + "\n\n"

  for food in menu:
    if food != ' ' and food != '-':
      tweet += food + "\n"

  api.update_status(tweet)