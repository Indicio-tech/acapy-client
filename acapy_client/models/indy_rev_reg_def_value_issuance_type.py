from enum import Enum


class IndyRevRegDefValueIssuanceType(str, Enum):
    ISSUANCE_ON_DEMAND = "ISSUANCE_ON_DEMAND"
    ISSUANCE_BY_DEFAULT = "ISSUANCE_BY_DEFAULT"

    def __str__(self) -> str:
        return str(self.value)
