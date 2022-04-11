from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.disclosures_disclosures_item import DisclosuresDisclosuresItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="Disclosures")


@attr.s(auto_attribs=True)
class Disclosures:
    """
    Attributes:
        disclosures (List[DisclosuresDisclosuresItem]): List of protocol or goal_code descriptors
        id (Union[Unset, str]): Message identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        type (Union[Unset, str]): Message type Example: https://didcomm.org/my-family/1.0/my-message-type.
    """

    disclosures: List[DisclosuresDisclosuresItem]
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        disclosures = []
        for disclosures_item_data in self.disclosures:
            disclosures_item = disclosures_item_data.to_dict()

            disclosures.append(disclosures_item)

        id = self.id
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "disclosures": disclosures,
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
        disclosures = []
        _disclosures = d.pop("disclosures")
        for disclosures_item_data in _disclosures:
            disclosures_item = DisclosuresDisclosuresItem.from_dict(disclosures_item_data)

            disclosures.append(disclosures_item)

        id = d.pop("@id", UNSET)

        type = d.pop("@type", UNSET)

        disclosures = cls(
            disclosures=disclosures,
            id=id,
            type=type,
        )

        disclosures.additional_properties = d
        return disclosures

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
