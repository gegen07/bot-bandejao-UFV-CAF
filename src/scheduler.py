# scheduling process
from apscheduler.schedulers.background import BlockingScheduler
from settings import SCHEDULE_BREAKFAST, SCHEDULE_LUNCH, SCHEDULE_DINER
from datetime import datetime, timedelta
import tweet 
import spider  

#scheduler to post Tweet
scheduler = BlockingScheduler({'apscheduler.timezone': 'America/Sao_Paulo'})

#  Using UTC time
scheduler.add_job(tweet.PostTweet, 
                  'cron', 
                  hour='5', 
                  kwargs={'time': SCHEDULE_BREAKFAST}) 
scheduler.add_job(tweet.PostTweet, 
                  'cron', 
                  hour='9',
                  minute='30', 
                  kwargs={'time': SCHEDULE_LUNCH})
scheduler.add_job(tweet.PostTweet, 
                  'cron', 
                  hour='16', 
                  kwargs={'time': SCHEDULE_DINER})

# schedule to get the data
scheduler.add_job(spider.Get_data, 'cron', day_of_week='5', hour='22')

scheduler.start()