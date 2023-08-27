import os
from dotenv import load_dotenv

load_dotenv()

class Constant:

    REDDIT_CLIENT_ID = os.environ["CLIENT_ID"]
    REDDIT_CLIENT_SECRET = os.environ["CLIENT_SECRET"]
    REDDIT_USERNAME = os.environ["USERNAME"]
    REDDIT_PASSWORD = os.environ["PASSWORD"]



    