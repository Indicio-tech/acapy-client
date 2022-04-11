from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtocolDescriptor")


@attr.s(auto_attribs=True)
class ProtocolDescriptor:
    """
    Attributes:
        pid (str):
        roles (Union[Unset, None, List[str]]): List of roles
    """

    pid: str
    roles: Union[Unset, None, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pid = self.pid
        roles: Union[Unset, None, List[str]] = UNSET
        if not isinstance(self.roles, Unset):
            if self.roles is None:
                roles = None
            else:
                roles = self.roles

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "pid": pid,
            }
        )
        if roles is not UNSET:
            field_dict["roles"] = roles

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pid = d.pop("pid")

        roles = cast(List[str], d.pop("roles", UNSET))

        protocol_descriptor = cls(
            pid=pid,
            roles=roles,
        )

        protocol_descriptor.additional_properties = d
        return protocol_descriptor

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
