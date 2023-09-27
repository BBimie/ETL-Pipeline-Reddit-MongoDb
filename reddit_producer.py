import os
from dotenv import load_dotenv
from kafka.producer import KafkaProducer
import json 
import praw
from sentiment_analysis import SentimentAnalysis
import datetime


load_dotenv()

REDDIT_CLIENT_ID = os.environ["REDDIT_CLIENT_ID"]
REDDIT_CLIENT_SECRET = os.environ["REDDIT_CLIENT_SECRET"]
REDDIT_USERNAME = os.environ["REDDIT_USERNAME"]
REDDIT_PASSWORD = os.environ["REDDIT_PASSWORD"]
SUBREDDIT_NAME=os.environ["SUBREDDIT_NAME"]


class RedditProducer:
    def __init__(self) -> None:
        pass

    def producer(self):
        """
        Create and return a Kafka producer instance.

        This function initializes a Kafka producer configured to connect to the Kafka broker at 'localhost:9092'
        with API version 0.11 or later. It also specifies a value serializer to encode values as JSON objects.

        Returns:
            producer: A configured Kafka producer instance.
        """
        try:
            producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 11), value_serializer=lambda v: json.dumps(v).encode('utf-8'))
            return producer
        except Exception as ex:
            print('Exception while connecting Kafka')
            print(str(ex))
            
    def _reddit(self):
        """
            Initialize and return a Reddit API client.

            This method initializes a Reddit API client using the provided Reddit client ID, client secret,
            and user agent. The user agent is typically in the format "app/v1". The initialized Reddit client
            can be used to interact with Reddit's API.

            Returns:
                praw.Reddit: An instance of the Reddit API client.
        """
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent="app/v1",
        )
        return reddit
    
    
    def stream_submissions(self, created_date:str) -> None:
        """ 
        :param 
            subreddit_name
            created_date: A string representing the date in 'YYYY-MM-DD' format 
        
        """
        producer = self.producer()

        subreddit = self._reddit().subreddit(SUBREDDIT_NAME).new(limit=None)

        for sub in subreddit:
            if datetime.datetime.utcfromtimestamp(sub.created_utc).strftime('%Y-%m-%d') >= created_date:
                entry: dict[str, str] = {
                       'title': str(sub.title),
                       'subreddit': str(sub.subreddit),
                       'author' : str(sub.author),
                       'created_date': datetime.datetime.utcfromtimestamp(sub.created_utc).strftime('%Y-%m-%d'),
                       'comments' : [ {'text': str(comment.body), 'author':str(comment.author) } for comment in sub.comments][:10],
                       'edited' : str(sub.edited),
                       'distinguished' : str(sub.distinguished),
                       'submission_id' : str(sub.id),
                       'num_comments' : str(sub.num_comments),
                       'over_18' : str(sub.over_18),
                       'submission_url' : str(sub.url),
                       'score' : str(sub.score),
                       'selftext' : SentimentAnalysis(submission=sub.selftext).clean_submission(),
                       'sentiment': SentimentAnalysis(submission=sub.selftext).label_sentiment(),
                       'spoiler' : str(sub.spoiler),
                       'upvote_ratio' : str(sub.upvote_ratio) 
                       }
                try:
                    producer.send("reddit_topic", value=entry)
                    print('Message published successfully.')
                except Exception as ex:
                    print(f'Exception in publishing message, {ex} ')
                    print(str(ex))

if __name__ == "__main__":
    #trigger producer
    producer = RedditProducer()
    try:
        input_date = input("Enter the date you want subreddits to start fetching from, YYYY-MM-DD: ")
        date_format = "%Y-%m-%d"
        formatted_date = datetime.datetime.strptime(input_date, date_format)

        #run project
        producer.stream_submissions(created_date=input_date)

    except ValueError:
        print("Invalid date format. Please restart enter the date in YYYY-MM-DD format. ")

    