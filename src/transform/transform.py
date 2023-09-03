import pandas as pd
import json
from kafka import KafkaConsumer

consumer = KafkaConsumer('redditcomments', bootstrap_servers=['localhost:9092'], api_version=(0,11,5),)

for msg in consumer:
    print (msg)