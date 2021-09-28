from enum import Enum


class V20PresExRecordVerified(str, Enum):
    TRUE = "True"
    FALSE = "False"

    def __str__(self) -> str:
        return str(self.value)
