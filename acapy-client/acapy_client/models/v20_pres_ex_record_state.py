from enum import Enum


class V20PresExRecordState(str, Enum):
    PROPOSAL_SENT = "proposal-sent"
    PROPOSAL_RECEIVED = "proposal-received"
    REQUEST_SENT = "request-sent"
    REQUEST_RECEIVED = "request-received"
    PRESENTATION_SENT = "presentation-sent"
    PRESENTATION_RECEIVED = "presentation-received"
    DONE = "done"
    ABANDONED = "abandoned"

    def __str__(self) -> str:
        return str(self.value)
