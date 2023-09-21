from kafka import KafkaConsumer
import json
from ..connections.mongodb_connection import MongoDBConnection


class RedditConsumer:
    def __init__(self) -> None:
        pass

    def consumer(self):
        consumer = KafkaConsumer('reddit_topic', 
                                 bootstrap_servers=['localhost:9092'],
                                 api_version=(0,11),)
        return consumer
    
    def consume_stream(self):
        DATA = []
        for msg in self.consumer():
            print(msg)
            print (msg)
            DATA.append(msg)
        return DATA
    
    # def load_data(self):
    #     MongoDBConnection().load_reddit_data()

data = RedditConsumer().consume_stream()



