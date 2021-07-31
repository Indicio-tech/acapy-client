from enum import Enum


class ConstraintsStatusRevoked(str, Enum):
    REQUIRED = "required"
    ALLOWED = "allowed"
    DISALLOWED = "disallowed"

    def __str__(self) -> str:
        return str(self.value)
