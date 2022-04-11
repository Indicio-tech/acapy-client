from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.menu_json import MenuJson

T = TypeVar("T", bound="SendMenu")


@attr.s(auto_attribs=True)
class SendMenu:
    """
    Attributes:
        menu (MenuJson):
    """

    menu: MenuJson
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        menu = self.menu.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "menu": menu,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        menu = MenuJson.from_dict(d.pop("menu"))

        send_menu = cls(
            menu=menu,
        )

        send_menu.additional_properties = d
        return send_menu

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
