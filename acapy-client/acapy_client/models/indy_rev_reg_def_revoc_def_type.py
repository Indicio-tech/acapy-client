from enum import Enum


class IndyRevRegDefRevocDefType(str, Enum):
    CL_ACCUM = "CL_ACCUM"

    def __str__(self) -> str:
        return str(self.value)
