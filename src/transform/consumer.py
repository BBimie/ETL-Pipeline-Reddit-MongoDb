import pandas as pd
from dotenv import load_dotenv
import os
import json
from kafka import KafkaConsumer
from ..connections.mongodb_connection import MongoDBConnection


class RedditConsumer:
    def __init__(self) -> None:
        pass

    def consumer(self):
        consumer = KafkaConsumer('redditcomments', 
                                 bootstrap_servers=['localhost:9092'],
                                 api_version=(0,11,5),)
        return consumer
    
    def consume_stream(self):
        DATA = []
        for msg in self.consumer():
            print (msg)
            DATA.append(msg)
        return DATA
    
    def load_data(self):
        MongoDBConnection().load_reddit_data()



