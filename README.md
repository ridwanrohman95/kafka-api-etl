## Kafka API ETL Pipeline

This project demonstrates a Kafka-based ETL pipeline using Python and Docker.

### Architecture
Public API → Kafka Producer → Kafka Topic → Consumer → Transform

### Run
docker-compose up --build

### Concepts
- Asynchronous ingestion
- Message queues
- ETL separation
- Dockerized services
- Shared libraries
- Testable transformations
