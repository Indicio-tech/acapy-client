from enum import Enum


class RevokeRequestNotifyVersion(str, Enum):
    V1_0 = "v1_0"
    V2_0 = "v2_0"

    def __str__(self) -> str:
        return str(self.value)
