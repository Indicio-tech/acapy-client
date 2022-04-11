from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.menu import Menu
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActionMenuFetchResult")


@attr.s(auto_attribs=True)
class ActionMenuFetchResult:
    """
    Attributes:
        result (Union[Unset, Menu]):
    """

    result: Union[Unset, Menu] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _result = d.pop("result", UNSET)
        result: Union[Unset, Menu]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = Menu.from_dict(_result)

        action_menu_fetch_result = cls(
            result=result,
        )

        action_menu_fetch_result.additional_properties = d
        return action_menu_fetch_result

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
