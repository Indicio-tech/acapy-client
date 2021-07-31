from enum import Enum


class IssuerRevRegRecordRevocDefType(str, Enum):
    CL_ACCUM = "CL_ACCUM"

    def __str__(self) -> str:
        return str(self.value)
