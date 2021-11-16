from enum import Enum


class CreateWalletRequestKeyManagementMode(str, Enum):
    MANAGED = "managed"

    def __str__(self) -> str:
        return str(self.value)
