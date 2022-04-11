from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.schema_input_descriptor import SchemaInputDescriptor
from ..types import UNSET, Unset

T = TypeVar("T", bound="SchemasInputDescriptorFilter")


@attr.s(auto_attribs=True)
class SchemasInputDescriptorFilter:
    """
    Attributes:
        oneof_filter (Union[Unset, bool]): oneOf
        uri_groups (Union[Unset, List[List[SchemaInputDescriptor]]]):
    """

    oneof_filter: Union[Unset, bool] = UNSET
    uri_groups: Union[Unset, List[List[SchemaInputDescriptor]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        oneof_filter = self.oneof_filter
        uri_groups: Union[Unset, List[List[Dict[str, Any]]]] = UNSET
        if not isinstance(self.uri_groups, Unset):
            uri_groups = []
            for uri_groups_item_data in self.uri_groups:
                uri_groups_item = []
                for uri_groups_item_item_data in uri_groups_item_data:
                    uri_groups_item_item = uri_groups_item_item_data.to_dict()

                    uri_groups_item.append(uri_groups_item_item)

                uri_groups.append(uri_groups_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if oneof_filter is not UNSET:
            field_dict["oneof_filter"] = oneof_filter
        if uri_groups is not UNSET:
            field_dict["uri_groups"] = uri_groups

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        oneof_filter = d.pop("oneof_filter", UNSET)

        uri_groups = []
        _uri_groups = d.pop("uri_groups", UNSET)
        for uri_groups_item_data in _uri_groups or []:
            uri_groups_item = []
            _uri_groups_item = uri_groups_item_data
            for uri_groups_item_item_data in _uri_groups_item:
                uri_groups_item_item = SchemaInputDescriptor.from_dict(uri_groups_item_item_data)

                uri_groups_item.append(uri_groups_item_item)

            uri_groups.append(uri_groups_item)

        schemas_input_descriptor_filter = cls(
            oneof_filter=oneof_filter,
            uri_groups=uri_groups,
        )

        schemas_input_descriptor_filter.additional_properties = d
        return schemas_input_descriptor_filter

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
