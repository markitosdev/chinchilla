import time
import random

from src.business.get_transaction_to_send import get_transaction_to_send
from src.business.send_transaction_to_kafka import send_transaction_to_kafka
from src.models.single.Transaction import Transaction
from pandas.errors import InvalidIndexError



def app():
    while True:
        index: int = 0
        try:
            transaction: Transaction = get_transaction_to_send(index)
        except InvalidIndexError:
            break
        send_transaction_to_kafka(transaction)
        index += 1
        random_wait: float = round(random.uniform(0.01, 60), 2)
        time.sleep(random_wait)