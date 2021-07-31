from enum import Enum


class ConstraintsSubjectIsIssuer(str, Enum):
    REQUIRED = "required"
    PREFERRED = "preferred"

    def __str__(self) -> str:
        return str(self.value)
