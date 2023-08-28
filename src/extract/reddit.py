import requests
import requests.auth
import os
from dotenv import load_dotenv
import json 

load_dotenv()

REDDIT_CLIENT_ID = os.environ["CLIENT_ID"]
REDDIT_CLIENT_SECRET = os.environ["CLIENT_SECRET"]
REDDIT_USERNAME = os.environ["USERNAME"]
REDDIT_PASSWORD = os.environ["PASSWORD"]

def reddit_api():
    #authenticate reddit app
    client_auth = requests.auth.HTTPBasicAuth(REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET)
    post_data = {'grant_type': 'password', 
                 'username': REDDIT_USERNAME, 
                 'password': REDDIT_PASSWORD}
    headers = {'User-Agent' : 'a script that pulls data from the Reddit API'}

    #send request to get the access token
    resp = requests.post('https://www.reddit.com/api/v1/access_token', 
                    auth=client_auth, 
                    data=post_data, 
                    headers=headers)
    
    if resp.status_code == 200:
        token = resp.json()['access_token']
        headers = {**headers, **{'Authorization' : f'Bearer {token}' }}
        return headers

    else:
        print('Error', resp)
        pass

# headers = get_access_token()

def get_raw_data():
    headers=reddit_api()
    resp = requests.get('https://oauth.reddit.com/r/AmItheAsshole?/hot', headers=headers ).json()
    #print(resp)
    return resp

def store_data():
    data = get_raw_data()
    save_file = open("data.json", "w")  
    json.dump(data, save_file, indent = 4)

store_data()
