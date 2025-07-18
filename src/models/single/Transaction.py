
from pydantic import BaseModel

from src.constants.TransactionType import TransactionType


class Transaction(BaseModel):
    step: int
    type: TransactionType
    amount: float
    nameOrig: str
    oldbalanceOrg: float
    newbalanceOrig: float
    nameDest: str
    oldbalanceDest: float
    newbalanceDest: float
    isFraud: int