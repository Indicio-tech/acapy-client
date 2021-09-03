from enum import Enum


class GetConnectionsState(str, Enum):
    ABANDONED = "abandoned"
    RESPONSE = "response"
    ACTIVE = "active"
    ERROR = "error"
    COMPLETED = "completed"
    INVITATION = "invitation"
    REQUEST = "request"
    INIT = "init"
    START = "start"

    def __str__(self) -> str:
        return str(self.value)
