import os
from dotenv import load_dotenv
from kafka import KafkaProducer
import json 
import praw
from datetime import datetime
from transform.sentiment_analysis import SentimentAnalysis

load_dotenv()

REDDIT_CLIENT_ID = os.environ["REDDIT_CLIENT_ID"]
REDDIT_CLIENT_SECRET = os.environ["REDDIT_CLIENT_SECRET"]
REDDIT_USERNAME = os.environ["REDDIT_USERNAME"]
REDDIT_PASSWORD = os.environ["REDDIT_PASSWORD"]



class RedditProducer:
    def __init__(self) -> None:
        pass

    def producer(self):
        try:
            producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 11))
            return producer
        except Exception as ex:
            print('Exception while connecting Kafka')
            print(str(ex))
            

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
        producer = self.producer()

        subreddit = self._reddit().subreddit(subreddit_name).new(limit=None)

        for sub in subreddit:
            if datetime.utcfromtimestamp(sub.created_utc).strftime('%Y-%m-%d') > created_date:
                sub: dict[str, str] = {
                       'title': sub.title,
                       'subreddit': sub.subreddit,
                       'author' : sub.author,
                       'created_date': datetime.utcfromtimestamp(sub.created_utc).strftime('%Y-%m-%d'),
                       'comments' : [ {'text': comment.body, 'author':comment.author } for comment in sub.comments][:10],
                       'edited' : sub.edited,
                       'distinguished' : sub.distinguished,
                       'submission_id' : sub.id,
                       'num_comments' : sub.num_comments,
                       'over_18' : sub.over_18,
                       'submission_url' : sub.url,
                       'score' : sub.score,
                       'selftext' : sub.selftext,
                       'sentiment': SentimentAnalysis(submission=sub.selftext).label_sentiment(),
                       'spoiler' : sub.spoiler,
                       'upvote_ratio' : sub.upvote_ratio}
                try:
                    producer.send("reddit", value=sub)
                    producer.flush()
                    print('Message published successfully.')
                except Exception as ex:
                    print('Exception in publishing message')
                    print(str(ex))

                
RedditProducer().stream_submissions(subreddit_name='Nigeria', created_date='2023-08-31')



