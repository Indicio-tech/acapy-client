from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.admin_config_config import AdminConfigConfig
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminConfig")


@attr.s(auto_attribs=True)
class AdminConfig:
    """
    Attributes:
        config (Union[Unset, AdminConfigConfig]): Configuration settings
    """

    config: Union[Unset, AdminConfigConfig] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        config: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _config = d.pop("config", UNSET)
        config: Union[Unset, AdminConfigConfig]
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = AdminConfigConfig.from_dict(_config)

        admin_config = cls(
            config=config,
        )

        admin_config.additional_properties = d
        return admin_config

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
