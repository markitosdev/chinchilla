from enum import Enum
from typing import Annotated
from pydantic import AfterValidator

class TransactionTypes(Enum):
    CASH_OUT = "CASH_OUT"
    CASH_IN = "CASH_IN"
    PAYMENT = "PAYMENT"


def transform_transaction_type_to_string(customerType: TransactionTypes) -> str:
    return customerType.value


TransactionType = Annotated[TransactionTypes, AfterValidator(transform_transaction_type_to_string)]
