from enum import Enum


class GetConnectionsState(str, Enum):
    COMPLETED = "completed"
    START = "start"
    RESPONSE = "response"
    REQUEST = "request"
    ERROR = "error"
    INIT = "init"
    INVITATION = "invitation"
    ACTIVE = "active"
    ABANDONED = "abandoned"

    def __str__(self) -> str:
        return str(self.value)
