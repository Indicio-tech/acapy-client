from enum import Enum


class GetConnectionsState(str, Enum):
    START = "start"
    COMPLETED = "completed"
    ERROR = "error"
    ABANDONED = "abandoned"
    INIT = "init"
    RESPONSE = "response"
    REQUEST = "request"
    INVITATION = "invitation"
    ACTIVE = "active"

    def __str__(self) -> str:
        return str(self.value)
