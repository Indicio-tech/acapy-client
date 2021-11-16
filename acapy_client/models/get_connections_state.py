from enum import Enum


class GetConnectionsState(str, Enum):
    RESPONSE = "response"
    START = "start"
    INIT = "init"
    ERROR = "error"
    ACTIVE = "active"
    ABANDONED = "abandoned"
    COMPLETED = "completed"
    INVITATION = "invitation"
    REQUEST = "request"

    def __str__(self) -> str:
        return str(self.value)
