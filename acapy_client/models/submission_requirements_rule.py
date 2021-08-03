from enum import Enum


class SubmissionRequirementsRule(str, Enum):
    ALL = "all"
    PICK = "pick"

    def __str__(self) -> str:
        return str(self.value)
