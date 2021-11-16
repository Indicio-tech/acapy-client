from enum import Enum


class CreateWalletRequestWalletType(str, Enum):
    ASKAR = "askar"
    IN_MEMORY = "in_memory"
    INDY = "indy"

    def __str__(self) -> str:
        return str(self.value)
