from settings import SCHEDULE_BREAKFAST, SCHEDULE_LUNCH, SCHEDULE_DINER
from datetime import datetime, timedelta
import tweet 
import spider

if __name__ == "__main__":
  spider.Get_data()
  tweet.PostTweet(SCHEDULE_DINER)