from enum import Enum


class GetConnectionsState(str, Enum):
    ERROR = "error"
    START = "start"
    ABANDONED = "abandoned"
    ACTIVE = "active"
    INVITATION = "invitation"
    RESPONSE = "response"
    INIT = "init"
    COMPLETED = "completed"
    REQUEST = "request"

    def __str__(self) -> str:
        return str(self.value)
