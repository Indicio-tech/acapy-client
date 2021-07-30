from enum import Enum


class IndyPresPredSpecPredicate(str, Enum):
    VALUE_0 = "<"
    VALUE_1 = "<="
    VALUE_2 = ">="
    VALUE_3 = ">"

    def __str__(self) -> str:
        return str(self.value)
