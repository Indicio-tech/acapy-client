from enum import Enum


class GetConnectionsConnectionProtocol(str, Enum):
    CONNECTIONS10 = "connections/1.0"
    DIDEXCHANGE10 = "didexchange/1.0"

    def __str__(self) -> str:
        return str(self.value)
