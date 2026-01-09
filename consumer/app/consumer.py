import json
from kafka import KafkaConsumer
from transform import transform_price

consumer = KafkaConsumer(
    "prices",
    bootstrap_servers="kafka:9092",
    value_deserializer=lambda v: json.loads(v.decode("utf-8"))
)

for msg in consumer:
    transformed = transform_price(msg.value)
    print(transformed)