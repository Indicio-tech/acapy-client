from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.attach_decorator_data_json import AttachDecoratorDataJson
from ..models.attach_decorator_data_jws import AttachDecoratorDataJWS
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachDecoratorData")


@attr.s(auto_attribs=True)
class AttachDecoratorData:
    """
    Attributes:
        base64 (Union[Unset, str]): Base64-encoded data Example: ey4uLn0=.
        json (Union[Unset, AttachDecoratorDataJson]): JSON-serialized data Example: {"sample": "content"}.
        jws (Union[Unset, AttachDecoratorDataJWS]):
        links (Union[Unset, List[str]]): List of hypertext links to data
        sha256 (Union[Unset, str]): SHA256 hash (binhex encoded) of content Example:
            617a48c7c8afe0521efdc03e5bb0ad9e655893e6b4b51f0e794d70fba132aacb.
    """

    base64: Union[Unset, str] = UNSET
    json: Union[Unset, AttachDecoratorDataJson] = UNSET
    jws: Union[Unset, AttachDecoratorDataJWS] = UNSET
    links: Union[Unset, List[str]] = UNSET
    sha256: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        base64 = self.base64
        json: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.json, Unset):
            json = self.json.to_dict()

        jws: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.jws, Unset):
            jws = self.jws.to_dict()

        links: Union[Unset, List[str]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links

        sha256 = self.sha256

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if base64 is not UNSET:
            field_dict["base64"] = base64
        if json is not UNSET:
            field_dict["json"] = json
        if jws is not UNSET:
            field_dict["jws"] = jws
        if links is not UNSET:
            field_dict["links"] = links
        if sha256 is not UNSET:
            field_dict["sha256"] = sha256

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        base64 = d.pop("base64", UNSET)

        _json = d.pop("json", UNSET)
        json: Union[Unset, AttachDecoratorDataJson]
        if isinstance(_json, Unset):
            json = UNSET
        else:
            json = AttachDecoratorDataJson.from_dict(_json)

        _jws = d.pop("jws", UNSET)
        jws: Union[Unset, AttachDecoratorDataJWS]
        if isinstance(_jws, Unset):
            jws = UNSET
        else:
            jws = AttachDecoratorDataJWS.from_dict(_jws)

        links = cast(List[str], d.pop("links", UNSET))

        sha256 = d.pop("sha256", UNSET)

        attach_decorator_data = cls(
            base64=base64,
            json=json,
            jws=jws,
            links=links,
            sha256=sha256,
        )

        attach_decorator_data.additional_properties = d
        return attach_decorator_data

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
