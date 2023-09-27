from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient

load_dotenv()

MONGODB_USER = os.environ['MONGODB_USER']
MONGODB_PASSWORD = os.environ['MONGODB_PASSWORD']
SUBREDDIT_NAME=os.environ["SUBREDDIT_NAME"]
MONGODB_CLUSTER = os.environ["MONGODB_CLUSTER"]
DATABASE = os.environ["DATABASE"]


class MongoDBConnection:
    def __init__(self) -> None:
        self.MONGODB_URI = f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_CLUSTER}.hnctuvt.mongodb.net/?retryWrites=true&w=majority"
        self.collection_name = SUBREDDIT_NAME
        self.database = DATABASE

    def client(self):
        # Create a new client and connect to the server
        client = MongoClient(self.MONGODB_URI, )
        return client

    def test_connection(self):
        # Send a ping to confirm a successful connection
        client = MongoClient(self.MONGODB_URI)
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            # print('could not test connection ', e)
            raise e

    def connect_collection(self):
        client = self.client()
        DB = client[self.database]

        #check if collection already exists?
        existing_collections = DB.list_collection_names()
        if self.collection_name in existing_collections:
            print(f"Collection '{self.collection_name}' already exists.")

        else:
            print(f'Collection {self.collection_name} does not exist.')
            # Create the collection
            try:
                collection = DB[self.collection_name]
                print(f"Collection '{self.collection_name}' created successfully.")
            except:
                print(f"Collection '{self.collection_name}' creation failed")
                pass

        
    def load_data(self, data):
        client = self.client()
        DB = client.reddit_db
        self.connect_collection()

        try:
            collection = DB[self.collection_name]
            collection.insert_one(data)
            print('Submission loaded into DB')
        
        except Exception as e:
            print('Could not load data into DB, ', e)



MongoDBConnection().connect_collection()