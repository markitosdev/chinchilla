from datetime import datetime

import pandas as pd

from src.models.data_frame.Transactions import Transactions
from pandas import DataFrame
from pykafka import KafkaClient
import threading

from src.models.single.Transaction import Transaction

KAFKA_HOST = "localhost:9092"
TOPIC = "test"

def send_transaction_to_kafka(transaction: Transaction) -> None:
    client = KafkaClient(hosts=KAFKA_HOST)
    topic = client.topics[TOPIC]
    with topic.get_sync_producer() as producer:
        producer.produce(str(transaction.model_dump()).encode("utf-8"), timestamp=datetime.now())
    return