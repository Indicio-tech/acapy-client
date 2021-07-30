from enum import Enum


class DIDCreateMethod(str, Enum):
    KEY = "key"
    SOV = "sov"

    def __str__(self) -> str:
        return str(self.value)
