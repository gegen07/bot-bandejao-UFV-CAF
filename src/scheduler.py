# scheduling process
from apscheduler.schedulers.background import BackgroundScheduler
from settings import SCHEDULE_BREAKFAST, SCHEDULE_LUNCH, SCHEDULE_DINER
from datetime import datetime, timedelta
import tweet 
import spider

#scheduler to post Tweet
if __name__ == "__main__":
  scheduler = BackgroundScheduler()

  #  Using UTC time
  scheduler.add_job(tweet.PostTweet(SCHEDULE_BREAKFAST), 'cron', hour='8') 
  scheduler.add_job(tweet.PostTweet(SCHEDULE_LUNCH), 'cron', hour='12', minute='30')
  scheduler.add_job(tweet.PostTweet(SCHEDULE_DINER), 'cron', hour='19')

  # schedule to get the data
  scheduler.add_job(spider.Get_data(), 'cron', day='sat', hour='22')