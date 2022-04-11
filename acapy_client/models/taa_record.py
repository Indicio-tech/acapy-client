from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TAARecord")


@attr.s(auto_attribs=True)
class TAARecord:
    """
    Attributes:
        digest (Union[Unset, str]):
        text (Union[Unset, str]):
        version (Union[Unset, str]):
    """

    digest: Union[Unset, str] = UNSET
    text: Union[Unset, str] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        digest = self.digest
        text = self.text
        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if digest is not UNSET:
            field_dict["digest"] = digest
        if text is not UNSET:
            field_dict["text"] = text
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        digest = d.pop("digest", UNSET)

        text = d.pop("text", UNSET)

        version = d.pop("version", UNSET)

        taa_record = cls(
            digest=digest,
            text=text,
            version=version,
        )

        taa_record.additional_properties = d
        return taa_record

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
