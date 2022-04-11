from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cred_def_value_primary import CredDefValuePrimary
from ..models.cred_def_value_revocation import CredDefValueRevocation
from ..types import UNSET, Unset

T = TypeVar("T", bound="CredDefValue")


@attr.s(auto_attribs=True)
class CredDefValue:
    """
    Attributes:
        primary (Union[Unset, CredDefValuePrimary]):
        revocation (Union[Unset, CredDefValueRevocation]):
    """

    primary: Union[Unset, CredDefValuePrimary] = UNSET
    revocation: Union[Unset, CredDefValueRevocation] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        primary: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.primary, Unset):
            primary = self.primary.to_dict()

        revocation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.revocation, Unset):
            revocation = self.revocation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if primary is not UNSET:
            field_dict["primary"] = primary
        if revocation is not UNSET:
            field_dict["revocation"] = revocation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _primary = d.pop("primary", UNSET)
        primary: Union[Unset, CredDefValuePrimary]
        if isinstance(_primary, Unset):
            primary = UNSET
        else:
            primary = CredDefValuePrimary.from_dict(_primary)

        _revocation = d.pop("revocation", UNSET)
        revocation: Union[Unset, CredDefValueRevocation]
        if isinstance(_revocation, Unset):
            revocation = UNSET
        else:
            revocation = CredDefValueRevocation.from_dict(_revocation)

        cred_def_value = cls(
            primary=primary,
            revocation=revocation,
        )

        cred_def_value.additional_properties = d
        return cred_def_value

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
