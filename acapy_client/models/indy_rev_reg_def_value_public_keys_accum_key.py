from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyRevRegDefValuePublicKeysAccumKey")


@attr.s(auto_attribs=True)
class IndyRevRegDefValuePublicKeysAccumKey:
    """
    Attributes:
        z (Union[Unset, str]): Value for z Example: 1 120F522F81E6B7 1 09F7A59005C4939854.
    """

    z: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        z = self.z

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if z is not UNSET:
            field_dict["z"] = z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        z = d.pop("z", UNSET)

        indy_rev_reg_def_value_public_keys_accum_key = cls(
            z=z,
        )

        indy_rev_reg_def_value_public_keys_accum_key.additional_properties = d
        return indy_rev_reg_def_value_public_keys_accum_key

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
