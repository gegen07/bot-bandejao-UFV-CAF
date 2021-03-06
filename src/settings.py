from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
from pathlib import Path  # python3 only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

import os
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_SECRET_API_KEY = os.getenv("TWITTER_SECRET_API_KEY")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET_TOKEN = os.getenv("TWITTER_ACCESS_SECRET_TOKEN")

import datetime
SCHEDULE_BREAKFAST = datetime.time(5,0,0)
SCHEDULE_LUNCH = datetime.time(9,30,0)
SCHEDULE_DINER = datetime.time(16,0,0) 