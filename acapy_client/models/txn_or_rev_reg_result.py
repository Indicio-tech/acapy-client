from typing import Any, Dict, Type, TypeVar, Union

import attr

from ..models.rev_reg_result import RevRegResult
from ..models.transaction_record import TransactionRecord
from ..types import UNSET, Unset

T = TypeVar("T", bound="TxnOrRevRegResult")


@attr.s(auto_attribs=True)
class TxnOrRevRegResult:
    """
    Attributes:
        sent (Union[Unset, RevRegResult]):
        txn (Union[Unset, TransactionRecord]):
    """

    sent: Union[Unset, RevRegResult] = UNSET
    txn: Union[Unset, TransactionRecord] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        sent: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sent, Unset):
            sent = self.sent.to_dict()

        txn: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.txn, Unset):
            txn = self.txn.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if sent is not UNSET:
            field_dict["sent"] = sent
        if txn is not UNSET:
            field_dict["txn"] = txn

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _sent = d.pop("sent", UNSET)
        sent: Union[Unset, RevRegResult]
        if isinstance(_sent, Unset):
            sent = UNSET
        else:
            sent = RevRegResult.from_dict(_sent)

        _txn = d.pop("txn", UNSET)
        txn: Union[Unset, TransactionRecord]
        if isinstance(_txn, Unset):
            txn = UNSET
        else:
            txn = TransactionRecord.from_dict(_txn)

        txn_or_rev_reg_result = cls(
            sent=sent,
            txn=txn,
        )

        return txn_or_rev_reg_result
