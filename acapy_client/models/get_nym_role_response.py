from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_nym_role_response_role import GetNymRoleResponseRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetNymRoleResponse")


@attr.s(auto_attribs=True)
class GetNymRoleResponse:
    """
    Attributes:
        role (Union[Unset, GetNymRoleResponseRole]): Ledger role Example: ENDORSER.
    """

    role: Union[Unset, GetNymRoleResponseRole] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if role is not UNSET:
            field_dict["role"] = role

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _role = d.pop("role", UNSET)
        role: Union[Unset, GetNymRoleResponseRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = GetNymRoleResponseRole(_role)

        get_nym_role_response = cls(
            role=role,
        )

        get_nym_role_response.additional_properties = d
        return get_nym_role_response

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
