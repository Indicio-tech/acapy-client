from enum import Enum


class CreateWalletRequestWalletDispatchType(str, Enum):
    DEFAULT = "default"
    BOTH = "both"
    BASE = "base"

    def __str__(self) -> str:
        return str(self.value)
