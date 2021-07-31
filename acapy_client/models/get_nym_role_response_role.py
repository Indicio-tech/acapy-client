from enum import Enum


class GetNymRoleResponseRole(str, Enum):
    STEWARD = "STEWARD"
    TRUSTEE = "TRUSTEE"
    ENDORSER = "ENDORSER"
    NETWORK_MONITOR = "NETWORK_MONITOR"
    USER = "USER"
    ROLE_REMOVE = "ROLE_REMOVE"

    def __str__(self) -> str:
        return str(self.value)
