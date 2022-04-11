from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.did_create_method import DIDCreateMethod
from ..models.did_create_options import DIDCreateOptions
from ..types import UNSET, Unset

T = TypeVar("T", bound="DIDCreate")


@attr.s(auto_attribs=True)
class DIDCreate:
    """
    Attributes:
        method (Union[Unset, DIDCreateMethod]):  Example: sov.
        options (Union[Unset, DIDCreateOptions]):
    """

    method: Union[Unset, DIDCreateMethod] = UNSET
    options: Union[Unset, DIDCreateOptions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _method = d.pop("method", UNSET)
        method: Union[Unset, DIDCreateMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = DIDCreateMethod(_method)

        _options = d.pop("options", UNSET)
        options: Union[Unset, DIDCreateOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = DIDCreateOptions.from_dict(_options)

        did_create = cls(
            method=method,
            options=options,
        )

        did_create.additional_properties = d
        return did_create

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
