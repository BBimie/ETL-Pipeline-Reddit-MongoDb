# ETL PIPELINE REDDIT TO MONGODB

This project aims to create an ETL (Extract, Transform, Load) pipeline for extracting data from Reddit through its API and storing it in a MongoDB database. Reddit is a popular platform with a vast amount of user-generated content, making it an excellent source of data for various purposes, including research, analysis, and data-driven decision-making.

This repository provides the necessary tools and scripts to perform the following key tasks:

**Data Extraction**: The ETL pipeline extracts data from specific subreddits on Reddit, allowing you to focus on topics of interest or relevance to your project.

**Data Transformation**: The extracted data is processed and transformed to ensure consistency and relevance. This includes some cleaning, filtering, text processing and sentiment analysis.

**Data Loading**: The transformed data is then loaded into a MongoDB database for storage and future analysis. MongoDB is a NoSQL database that offers flexibility and scalability for handling diverse data types.

By setting up this ETL pipeline, I have automated the process of collecting and managing Reddit data, making it easier to access and analyze some of the information needed. 

Whether conducting research, monitoring trends, or building applications that require Reddit data, this project provides a solid foundation for your data processing needs.



## RUN PROJECT

You need to have a Reddit account get Reddit API keys and also set up a MongoDB cluster on MongoDB Atlas. Then you can get to work.

1. Create virtualenv: I used Python 3.10 for this project.

    `virtualenv venv --python=python3.10`


    `source venv/usr/local/bin/activate`

2. (Optional if you already have kafka setup) Setup Kafka on Docker

    `bash kafka_setup.sh`

3. Install packages 

    `pip install -r requirements.txt`

4. Create and update environmental variables in `.env`

``` REDDIT_CLIENT_ID - Reddit API Client ID
    REDDIT_CLIENT_SECRET - Reddit API Client Secret
    REDDIT_USERNAME - Your Reddit Username
    REDDIT_PASSWORD - Your Reddit Password
    MONGODB_USER - Your MongoDB User
    MONGODB_PASSWORD - Your MongoDB password
    MONGODB_CLUSTER - MongoDB cluster that will host the data
    DATABASE - Database created on MongoDB to load the data into
    SUBREDDIT_NAME - the name of the subreddit you want to pull data from, which will also become the collection name
    KAFKA_TOPIC - Kafka topic
```
5. Open two separate terminals to run the kafka producer and consumer separately. Run the producer first
    - producer: 
    `python3 reddit_producer.py`
    - consumer: 
    `python3 consumer.py`

6. Enter your desired date and wait for the data to be pulled and loaded into the database.


## TOOLS AND TECHNOLOGIES

- Praw
- Kafka
- Pymongo
- MongoDB
- Docker
