from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="WriteLedgerRequest")


@attr.s(auto_attribs=True)
class WriteLedgerRequest:
    """
    Attributes:
        ledger_id (Union[Unset, str]):
    """

    ledger_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ledger_id = self.ledger_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ledger_id is not UNSET:
            field_dict["ledger_id"] = ledger_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ledger_id = d.pop("ledger_id", UNSET)

        write_ledger_request = cls(
            ledger_id=ledger_id,
        )

        write_ledger_request.additional_properties = d
        return write_ledger_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
