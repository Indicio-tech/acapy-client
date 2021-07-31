from enum import Enum


class ConstraintsStatusSuspended(str, Enum):
    REQUIRED = "required"
    ALLOWED = "allowed"
    DISALLOWED = "disallowed"

    def __str__(self) -> str:
        return str(self.value)
