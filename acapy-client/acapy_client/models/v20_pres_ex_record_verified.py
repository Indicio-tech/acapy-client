from enum import Enum


class V20PresExRecordVerified(str, Enum):
    TRUE = "true"
    FALSE = "false"

    def __str__(self) -> str:
        return str(self.value)
