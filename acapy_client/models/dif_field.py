from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.dif_field_predicate import DIFFieldPredicate
from ..models.filter_ import Filter
from ..types import UNSET, Unset

T = TypeVar("T", bound="DIFField")


@attr.s(auto_attribs=True)
class DIFField:
    """
    Attributes:
        filter_ (Union[Unset, Filter]):
        id (Union[Unset, str]): ID
        path (Union[Unset, List[str]]):
        predicate (Union[Unset, DIFFieldPredicate]): Preference
        purpose (Union[Unset, str]): Purpose
    """

    filter_: Union[Unset, Filter] = UNSET
    id: Union[Unset, str] = UNSET
    path: Union[Unset, List[str]] = UNSET
    predicate: Union[Unset, DIFFieldPredicate] = UNSET
    purpose: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        id = self.id
        path: Union[Unset, List[str]] = UNSET
        if not isinstance(self.path, Unset):
            path = self.path

        predicate: Union[Unset, str] = UNSET
        if not isinstance(self.predicate, Unset):
            predicate = self.predicate.value

        purpose = self.purpose

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if id is not UNSET:
            field_dict["id"] = id
        if path is not UNSET:
            field_dict["path"] = path
        if predicate is not UNSET:
            field_dict["predicate"] = predicate
        if purpose is not UNSET:
            field_dict["purpose"] = purpose

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, Filter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = Filter.from_dict(_filter_)

        id = d.pop("id", UNSET)

        path = cast(List[str], d.pop("path", UNSET))

        _predicate = d.pop("predicate", UNSET)
        predicate: Union[Unset, DIFFieldPredicate]
        if isinstance(_predicate, Unset):
            predicate = UNSET
        else:
            predicate = DIFFieldPredicate(_predicate)

        purpose = d.pop("purpose", UNSET)

        dif_field = cls(
            filter_=filter_,
            id=id,
            path=path,
            predicate=predicate,
            purpose=purpose,
        )

        dif_field.additional_properties = d
        return dif_field

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
