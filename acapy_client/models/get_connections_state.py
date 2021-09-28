from enum import Enum


class GetConnectionsState(str, Enum):
    INIT = "init"
    RESPONSE = "response"
    ERROR = "error"
    ABANDONED = "abandoned"
    ACTIVE = "active"
    START = "start"
    REQUEST = "request"
    COMPLETED = "completed"
    INVITATION = "invitation"

    def __str__(self) -> str:
        return str(self.value)
