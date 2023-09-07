from pymongo import MongoClient
from pymongo.server_api import ServerApi


MONGODB_USER = os.environ['MONGODB_USER']
MONGODB_PASSWORD = os.environ['MONGODB_PASSWORD']
MONGODB_URI = f"mongodb+srv://myAtlas{MONGODB_USER}:{MONGODB_PASSWORD}@myatlasclusteredu.xncbdmr.mongodb.net/?retryWrites=true&w=majority"

class MongoDBConnection:
    def __init__(self) -> None:
        pass

    def client(self):
        # Create a new client and connect to the server
        client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

    def test_connection(self):
        # Send a ping to confirm a successful connection
        client = self.client()
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def load_reddit_data(self):
        client = self.client()
        DB = client.reddit_db
        DB.submissions.insert_many()