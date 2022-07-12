from enum import Enum


class GetConnectionsState(str, Enum):
    ABANDONED = "abandoned"
    INVITATION = "invitation"
    ERROR = "error"
    COMPLETED = "completed"
    ACTIVE = "active"
    REQUEST = "request"
    INIT = "init"
    START = "start"
    RESPONSE = "response"

    def __str__(self) -> str:
        return str(self.value)
