from enum import Enum


class IndyGEProofPredPType(str, Enum):
    LT = "LT"
    LE = "LE"
    GE = "GE"
    GT = "GT"

    def __str__(self) -> str:
        return str(self.value)
