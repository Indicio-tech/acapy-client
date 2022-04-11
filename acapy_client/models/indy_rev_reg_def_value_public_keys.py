from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_rev_reg_def_value_public_keys_accum_key import IndyRevRegDefValuePublicKeysAccumKey
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyRevRegDefValuePublicKeys")


@attr.s(auto_attribs=True)
class IndyRevRegDefValuePublicKeys:
    """
    Attributes:
        accum_key (Union[Unset, IndyRevRegDefValuePublicKeysAccumKey]):
    """

    accum_key: Union[Unset, IndyRevRegDefValuePublicKeysAccumKey] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accum_key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accum_key, Unset):
            accum_key = self.accum_key.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accum_key is not UNSET:
            field_dict["accumKey"] = accum_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _accum_key = d.pop("accumKey", UNSET)
        accum_key: Union[Unset, IndyRevRegDefValuePublicKeysAccumKey]
        if isinstance(_accum_key, Unset):
            accum_key = UNSET
        else:
            accum_key = IndyRevRegDefValuePublicKeysAccumKey.from_dict(_accum_key)

        indy_rev_reg_def_value_public_keys = cls(
            accum_key=accum_key,
        )

        indy_rev_reg_def_value_public_keys.additional_properties = d
        return indy_rev_reg_def_value_public_keys

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
