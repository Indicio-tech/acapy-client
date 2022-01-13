from enum import Enum


class QueryItemFeatureType(str, Enum):
    PROTOCOL = "protocol"
    GOAL_CODE = "goal-code"

    def __str__(self) -> str:
        return str(self.value)
