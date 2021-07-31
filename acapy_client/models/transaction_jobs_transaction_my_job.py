from enum import Enum


class TransactionJobsTransactionMyJob(str, Enum):
    TRANSACTION_AUTHOR = "TRANSACTION_AUTHOR"
    TRANSACTION_ENDORSER = "TRANSACTION_ENDORSER"
    RESET = "reset"

    def __str__(self) -> str:
        return str(self.value)
