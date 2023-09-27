from kafka import KafkaConsumer
import json
from mongodb_connection import MongoDBConnection


class RedditConsumer:
    def __init__(self) -> None:
        pass

    def consumer(self):
        consumer = KafkaConsumer('reddit_topic', 
                                 bootstrap_servers=['localhost:9092'],
                                 api_version=(0,11),)
        return consumer
    
    def consume_stream(self):
        print('Consuming data')
        for msg in self.consumer():
            data = json.loads(msg.value.decode("utf-8"))
            print(data)
            print("====")
            self.load_data(data=data)
        
    
    def load_data(self, data):
        print('Loading data into database')
        MongoDBConnection().load_data(data=data)


if __name__ == "__main__":
    data = RedditConsumer().consume_stream()
