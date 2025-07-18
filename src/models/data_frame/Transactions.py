import pandera.pandas as pa
from pandera.typing.pandas import Index, DataFrame, Series

from src.constants.TransactionType import TransactionType


class Transactions(pa.DataFrameModel):
    step: Series[int]
    type: Series[TransactionType]
    amount: Series[float]
    nameOrig: Series[str]
    oldbalanceOrg: Series[float]
    newbalanceOrig: Series[float]
    nameDest: Series[str]
    oldbalanceDest: Series[float]
    newbalanceDest: Series[float]
    isFraud: Series[int] = pa.Field(isin=[0,1], nullable=False)