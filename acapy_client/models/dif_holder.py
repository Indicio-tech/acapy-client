from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.dif_holder_directive import DIFHolderDirective
from ..types import UNSET, Unset

T = TypeVar("T", bound="DIFHolder")


@attr.s(auto_attribs=True)
class DIFHolder:
    """
    Attributes:
        directive (Union[Unset, DIFHolderDirective]): Preference
        field_id (Union[Unset, List[str]]):
    """

    directive: Union[Unset, DIFHolderDirective] = UNSET
    field_id: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        directive: Union[Unset, str] = UNSET
        if not isinstance(self.directive, Unset):
            directive = self.directive.value

        field_id: Union[Unset, List[str]] = UNSET
        if not isinstance(self.field_id, Unset):
            field_id = self.field_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if directive is not UNSET:
            field_dict["directive"] = directive
        if field_id is not UNSET:
            field_dict["field_id"] = field_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _directive = d.pop("directive", UNSET)
        directive: Union[Unset, DIFHolderDirective]
        if isinstance(_directive, Unset):
            directive = UNSET
        else:
            directive = DIFHolderDirective(_directive)

        field_id = cast(List[str], d.pop("field_id", UNSET))

        dif_holder = cls(
            directive=directive,
            field_id=field_id,
        )

        dif_holder.additional_properties = d
        return dif_holder

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
