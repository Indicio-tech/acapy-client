from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.query_item import QueryItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="Queries")


@attr.s(auto_attribs=True)
class Queries:
    """
    Attributes:
        id (Union[Unset, str]): Message identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        type (Union[Unset, str]): Message type Example: https://didcomm.org/my-family/1.0/my-message-type.
        queries (Union[Unset, List[QueryItem]]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    queries: Union[Unset, List[QueryItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        queries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.queries, Unset):
            queries = []
            for queries_item_data in self.queries:
                queries_item = queries_item_data.to_dict()

                queries.append(queries_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["@id"] = id
        if type is not UNSET:
            field_dict["@type"] = type
        if queries is not UNSET:
            field_dict["queries"] = queries

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("@id", UNSET)

        type = d.pop("@type", UNSET)

        queries = []
        _queries = d.pop("queries", UNSET)
        for queries_item_data in _queries or []:
            queries_item = QueryItem.from_dict(queries_item_data)

            queries.append(queries_item)

        queries = cls(
            id=id,
            type=type,
            queries=queries,
        )

        queries.additional_properties = d
        return queries

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
