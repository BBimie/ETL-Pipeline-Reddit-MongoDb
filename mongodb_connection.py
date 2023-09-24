from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient

load_dotenv()


MONGODB_USER = os.environ['MONGODB_USER']
MONGODB_PASSWORD = os.environ['MONGODB_PASSWORD']


class MongoDBConnection:
    def __init__(self) -> None:
        self.MONGODB_URI = f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASSWORD}@redditcluster.hnctuvt.mongodb.net/?retryWrites=true&w=majority"

    def client(self):
        # Create a new client and connect to the server
        client = MongoClient(self.MONGODB_URI)
        return client

    def test_connection(self):
        # Send a ping to confirm a successful connection
        client = MongoClient(self.MONGODB_URI)
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print('could not test connection ', e)

    def load_reddit_data(self, data):
        client = self.client()
        DB = client.reddit_db
        try:
            DB.submissions.insert_many(data)
            print('Submission loaded into DB')
            
        except Exception as e:
            print('Could not load data into DB, ', e)

MongoDBConnection().test_connection()