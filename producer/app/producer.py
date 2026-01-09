import json
import time
from kafka import KafkaProducer
from api_client import fetch_price

producer = KafkaProducer(
    bootstrap_servers="kafka:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    data = fetch_price()
    producer.send("prices", data)
    time.sleep(10)
