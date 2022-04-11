from enum import Enum


class GetConnectionsConnectionProtocol(str, Enum):
    CONNECTIONS1_0 = "connections/1.0"
    DIDEXCHANGE1_0 = "didexchange/1.0"

    def __str__(self) -> str:
        return str(self.value)
