from enum import Enum


class CreateWalletRequestWalletKeyDerivation(str, Enum):
    ARGON2I_MOD = "ARGON2I_MOD"
    ARGON2I_INT = "ARGON2I_INT"
    RAW = "RAW"

    def __str__(self) -> str:
        return str(self.value)
