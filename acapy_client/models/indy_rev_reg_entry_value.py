from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyRevRegEntryValue")


@attr.s(auto_attribs=True)
class IndyRevRegEntryValue:
    """
    Attributes:
        accum (Union[Unset, str]): Accumulator value Example: 21 11792B036AED0AAA12A4 4 298B2571FFC63A737.
        prev_accum (Union[Unset, str]): Previous accumulator value Example: 21 137AC810975E4 6 76F0384B6F23.
        revoked (Union[Unset, List[int]]): Revoked credential revocation identifiers
    """

    accum: Union[Unset, str] = UNSET
    prev_accum: Union[Unset, str] = UNSET
    revoked: Union[Unset, List[int]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accum = self.accum
        prev_accum = self.prev_accum
        revoked: Union[Unset, List[int]] = UNSET
        if not isinstance(self.revoked, Unset):
            revoked = self.revoked

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accum is not UNSET:
            field_dict["accum"] = accum
        if prev_accum is not UNSET:
            field_dict["prevAccum"] = prev_accum
        if revoked is not UNSET:
            field_dict["revoked"] = revoked

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        accum = d.pop("accum", UNSET)

        prev_accum = d.pop("prevAccum", UNSET)

        revoked = cast(List[int], d.pop("revoked", UNSET))

        indy_rev_reg_entry_value = cls(
            accum=accum,
            prev_accum=prev_accum,
            revoked=revoked,
        )

        indy_rev_reg_entry_value.additional_properties = d
        return indy_rev_reg_entry_value

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
