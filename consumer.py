from kafka import KafkaConsumer
import json
from mongodb_connection import MongoDBConnection
import logging


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
            print(msg.value)
            print("====")
            DATA.append(msg)
        return DATA
    
    # def load_data(self):
    #     MongoDBConnection().load_reddit_data()


if __name__ == "__main__":
    data = RedditConsumer().consume_stream()
