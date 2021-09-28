from enum import Enum


class WalletRecordKeyManagementMode(str, Enum):
    MANAGED = "managed"
    UNMANAGED = "unmanaged"

    def __str__(self) -> str:
        return str(self.value)
