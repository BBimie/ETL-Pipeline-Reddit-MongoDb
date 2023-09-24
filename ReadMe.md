SCOPE:

REDDIT - MONGODB(THROUGH KAFKA - STREAMING) - GRAFANA (SENTIMENT ANALYSIS DASHBOARD) - ORCHESTRATED BY AIRFLOW - DOCKERIZED

- Fetch data daily (filter by date) - streaming included
- Load the needed data into MongoDB
- Carry out sentiment analysis (not suure of this part yet)
- GRAFANA COMES IN HERE ...
- AIRFLOW GUIDED
- DOCKER


** To Run **
- run: `chmod +x kafka_setup.sh`

- Create virtual environment

- Install dependences `pip install -r requirements.txt`

- Update environmental variables

- open two separate terminals to run the producer and consumer separately
    - producer: `python3 reddit_producer.py`
    - consumer: `python3 consumer.py`
