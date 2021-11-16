from enum import Enum


class GetPresentProof20RecordsRole(str, Enum):
    PROVER = "prover"
    VERIFIER = "verifier"

    def __str__(self) -> str:
        return str(self.value)
