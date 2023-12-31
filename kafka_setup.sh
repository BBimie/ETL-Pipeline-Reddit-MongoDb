# #!/bin/bash

source .env

# # Build and start Docker containers
docker-compose -f docker-compose.yml up -d

# # Wait for Kafka to be ready
until [ $(docker-compose logs kafka | grep -c 'started (kafka.server.KafkaServer)') -gt 0 ]; do
  echo "Waiting for Kafka to start..."
  sleep 1
done

# #Connect to Kafka shell
docker exec -it kafka /bin/sh

# # Create Kafka topic
echo "Creating Kafka topic > $KAFKA_TOPIC "
kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic $KAFKA_TOPIC


echo "Kafka setup complete."




