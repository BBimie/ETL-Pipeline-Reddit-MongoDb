from dotenv import load_dotenv
import os

from pymongo import MongoClient
from pymongo.server_api import ServerApi
import ssl

load_dotenv()


MONGODB_USER = os.environ['MONGODB_USER']
MONGODB_PASSWORD = os.environ['MONGODB_PASSWORD']
MONGODB_URI = f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASSWORD}@myatlasclusteredu.xncbdmr.mongodb.net/?retryWrites=true&w=majority"

class MongoDBConnection:
    def __init__(self) -> None:
        pass

    def client(self):
        # Create a new client and connect to the server
        client = MongoClient(MONGODB_URI, server_api=ServerApi('1'), ssl_cert_reqs=ssl.CERT_NONE)
        return client

    def test_connection(self):
        # Send a ping to confirm a successful connection
        client = self.client()
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def load_reddit_data(self, data):
        client = self.client()
        DB = client.reddit_db
        try:
            DB.submissions.insert_many(data)
            print('Submission loaded into DB')
            
        except Exception as e:
            print('Could not load data into DB, ', e)