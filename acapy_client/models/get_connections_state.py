from enum import Enum


class GetConnectionsState(str, Enum):
    INVITATION = "invitation"
    START = "start"
    RESPONSE = "response"
    ABANDONED = "abandoned"
    COMPLETED = "completed"
    REQUEST = "request"
    ERROR = "error"
    INIT = "init"
    ACTIVE = "active"

    def __str__(self) -> str:
        return str(self.value)
