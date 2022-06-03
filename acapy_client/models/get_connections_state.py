from enum import Enum


class GetConnectionsState(str, Enum):
    RESPONSE = "response"
    COMPLETED = "completed"
    START = "start"
    ABANDONED = "abandoned"
    ERROR = "error"
    REQUEST = "request"
    ACTIVE = "active"
    INVITATION = "invitation"
    INIT = "init"

    def __str__(self) -> str:
        return str(self.value)
