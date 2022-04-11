from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DIFOptions")


@attr.s(auto_attribs=True)
class DIFOptions:
    """
    Attributes:
        challenge (Union[Unset, str]): Challenge protect against replay attack Example:
            3fa85f64-5717-4562-b3fc-2c963f66afa6.
        domain (Union[Unset, str]): Domain protect against replay attack Example: 4jt78h47fh47.
    """

    challenge: Union[Unset, str] = UNSET
    domain: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        challenge = self.challenge
        domain = self.domain

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if challenge is not UNSET:
            field_dict["challenge"] = challenge
        if domain is not UNSET:
            field_dict["domain"] = domain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        challenge = d.pop("challenge", UNSET)

        domain = d.pop("domain", UNSET)

        dif_options = cls(
            challenge=challenge,
            domain=domain,
        )

        dif_options.additional_properties = d
        return dif_options

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
