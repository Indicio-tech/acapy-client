from enum import Enum


class DIDMethod(str, Enum):
    SOV = "sov"
    KEY = "key"

    def __str__(self) -> str:
        return str(self.value)
