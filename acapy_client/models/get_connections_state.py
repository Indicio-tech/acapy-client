from enum import Enum


class GetConnectionsState(str, Enum):
    ERROR = "error"
    ACTIVE = "active"
    INVITATION = "invitation"
    INIT = "init"
    START = "start"
    RESPONSE = "response"
    REQUEST = "request"
    COMPLETED = "completed"
    ABANDONED = "abandoned"

    def __str__(self) -> str:
        return str(self.value)
