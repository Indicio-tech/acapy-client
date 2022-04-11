from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.keylist_query_filter import KeylistQueryFilter
from ..models.keylist_query_paginate import KeylistQueryPaginate
from ..types import UNSET, Unset

T = TypeVar("T", bound="KeylistQuery")


@attr.s(auto_attribs=True)
class KeylistQuery:
    """
    Attributes:
        id (Union[Unset, str]): Message identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        type (Union[Unset, str]): Message type Example: https://didcomm.org/my-family/1.0/my-message-type.
        filter_ (Union[Unset, KeylistQueryFilter]): Query dictionary object Example: {'filter': {}}.
        paginate (Union[Unset, KeylistQueryPaginate]):
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    filter_: Union[Unset, KeylistQueryFilter] = UNSET
    paginate: Union[Unset, KeylistQueryPaginate] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        paginate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.paginate, Unset):
            paginate = self.paginate.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["@id"] = id
        if type is not UNSET:
            field_dict["@type"] = type
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if paginate is not UNSET:
            field_dict["paginate"] = paginate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("@id", UNSET)

        type = d.pop("@type", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, KeylistQueryFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = KeylistQueryFilter.from_dict(_filter_)

        _paginate = d.pop("paginate", UNSET)
        paginate: Union[Unset, KeylistQueryPaginate]
        if isinstance(_paginate, Unset):
            paginate = UNSET
        else:
            paginate = KeylistQueryPaginate.from_dict(_paginate)

        keylist_query = cls(
            id=id,
            type=type,
            filter_=filter_,
            paginate=paginate,
        )

        keylist_query.additional_properties = d
        return keylist_query

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
