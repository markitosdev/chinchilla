from src.file_handler.create_dataframe_from_csv import create_dataframe_from_csv
from src.models.data_frame.Transactions import Transactions
from src.models.single.Transaction import Transaction
from pandas import DataFrame, read_csv

def get_transaction_to_send(index) -> Transaction:
    transactions: DataFrame[Transactions] = create_dataframe_from_csv("src/assets/transactions.csv")
    transaction: Transaction = Transaction(**transactions.iloc[index].to_dict())
    return transaction
