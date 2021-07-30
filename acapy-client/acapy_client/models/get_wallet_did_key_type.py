from enum import Enum


class GetWalletDidKeyType(str, Enum):
    ED25519 = "ed25519"
    BLS12381G2 = "bls12381g2"

    def __str__(self) -> str:
        return str(self.value)
