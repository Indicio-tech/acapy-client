from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.protocol_descriptor import ProtocolDescriptor
from ..types import UNSET, Unset

T = TypeVar("T", bound="Disclose")


@attr.s(auto_attribs=True)
class Disclose:
    """
    Attributes:
        protocols (List[ProtocolDescriptor]): List of protocol descriptors
        id (Union[Unset, str]): Message identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        type (Union[Unset, str]): Message type Example: https://didcomm.org/my-family/1.0/my-message-type.
    """

    protocols: List[ProtocolDescriptor]
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        protocols = []
        for protocols_item_data in self.protocols:
            protocols_item = protocols_item_data.to_dict()

            protocols.append(protocols_item)

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "protocols": protocols,
            }
        )
        if id is not UNSET:
            field_dict["@id"] = id
        if type is not UNSET:
            field_dict["@type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        protocols = []
        _protocols = d.pop("protocols")
        for protocols_item_data in _protocols:
            protocols_item = ProtocolDescriptor.from_dict(protocols_item_data)

            protocols.append(protocols_item)

        id = d.pop("@id", UNSET)

        type = d.pop("@type", UNSET)

        disclose = cls(
            protocols=protocols,
            id=id,
            type=type,
        )

        disclose.additional_properties = d
        return disclose

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
