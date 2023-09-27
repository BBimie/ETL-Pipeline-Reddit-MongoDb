

** To Run **
-- Create virtualenv: 

- If you don't already have Kafka setup, you can set it up on Docker by running
`bash kafka_setup.sh`

- Create virtual environment: I used Python 3.10 for this project
`virtualenv venv --python=python3.10`

-- activate virtual environment
    `source venv/usr/local/bin/activate`

- Install dependences `pip install -r requirements.txt`

- Create and update environmental variables in `.env`
``` REDDIT_CLIENT_ID 
    REDDIT_CLIENT_SECRET
    REDDIT_USERNAME
    REDDIT_PASSWORD
    MONGODB_USER
    MONGODB_PASSWORD
    SUBREDDIT_NAME
```

- open two separate terminals to run the producer and consumer separately
    - producer: `python3 reddit_producer.py`
    - consumer: `python3 consumer.py`
