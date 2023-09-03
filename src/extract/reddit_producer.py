import os
from dotenv import load_dotenv
from kafka import KafkaProducer
import json 
import praw
from datetime import datetime

load_dotenv()

REDDIT_CLIENT_ID = os.environ["CLIENT_ID"]
REDDIT_CLIENT_SECRET = os.environ["CLIENT_SECRET"]
REDDIT_USERNAME = os.environ["USERNAME"]
REDDIT_PASSWORD = os.environ["PASSWORD"]



class RedditProducer:
    def __init__(self) -> None:
        pass

    def producer(self):
        return KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer=lambda x:json.dumps(x).encode('utf-8'),
                            api_version=(0,11,5)
                        )

    def _reddit(self):
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent="app/v1",
        )
        return reddit
    
    
    def stream_submissions(self, subreddit_name:str, created_date:str) -> None:
        """ 
        :param 
            subreddit_name
            created_date: A string representing the date in 'YYYY-MM-DD' format 
        
        """

        subreddit = self._reddit().subreddit(subreddit_name).new(limit=None)

        for sub in subreddit:
            if datetime.utcfromtimestamp(sub.created_utc).strftime('%Y-%m-%d') > created_date:
                sub: dict[str, str] = {
                       'title': sub.title,
                       'subreddit': sub.subreddit,
                       'author' : sub.author,
                       'created_date': datetime.utcfromtimestamp(sub.created_utc).strftime('%Y-%m-%d'),
                       'comments' : sub.comments,
                       'edited' : sub.edited,
                       'distinguished' : sub.distinguished,
                       'submission_id' : sub.id,
                       'num_comments' : sub.num_comments,
                       'over_18' : sub.over_18,
                       'submission_url' : sub.url,
                       'score' : sub.score,
                       'selftext' : sub.selftext,
                       'spoiler' : sub.spoiler,
                       'upvote_ratio' : sub.upvote_ratio}
                print(sub)
                d = self.producer().send("redditcomments", value=sub)
                meta = d.get()
                print(meta.topic)

                
RedditProducer().stream_submissions(subreddit_name='python', created_date='2023-08-01')



