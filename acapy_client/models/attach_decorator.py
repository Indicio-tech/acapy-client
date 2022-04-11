from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attach_decorator_data import AttachDecoratorData
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttachDecorator")


@attr.s(auto_attribs=True)
class AttachDecorator:
    """
    Attributes:
        data (AttachDecoratorData):
        id (Union[Unset, str]): Attachment identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        byte_count (Union[Unset, int]): Byte count of data included by reference Example: 1234.
        description (Union[Unset, str]): Human-readable description of content Example: view from doorway, facing east,
            with lights off.
        filename (Union[Unset, str]): File name Example: IMG1092348.png.
        lastmod_time (Union[Unset, str]): Hint regarding last modification datetime, in ISO-8601 format Example:
            2021-12-31 23:59:59+00:00.
        mime_type (Union[Unset, str]): MIME type Example: image/png.
    """

    data: AttachDecoratorData
    id: Union[Unset, str] = UNSET
    byte_count: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    lastmod_time: Union[Unset, str] = UNSET
    mime_type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data = self.data.to_dict()

        id = self.id
        byte_count = self.byte_count
        description = self.description
        filename = self.filename
        lastmod_time = self.lastmod_time
        mime_type = self.mime_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if id is not UNSET:
            field_dict["@id"] = id
        if byte_count is not UNSET:
            field_dict["byte_count"] = byte_count
        if description is not UNSET:
            field_dict["description"] = description
        if filename is not UNSET:
            field_dict["filename"] = filename
        if lastmod_time is not UNSET:
            field_dict["lastmod_time"] = lastmod_time
        if mime_type is not UNSET:
            field_dict["mime-type"] = mime_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data = AttachDecoratorData.from_dict(d.pop("data"))

        id = d.pop("@id", UNSET)

        byte_count = d.pop("byte_count", UNSET)

        description = d.pop("description", UNSET)

        filename = d.pop("filename", UNSET)

        lastmod_time = d.pop("lastmod_time", UNSET)

        mime_type = d.pop("mime-type", UNSET)

        attach_decorator = cls(
            data=data,
            id=id,
            byte_count=byte_count,
            description=description,
            filename=filename,
            lastmod_time=lastmod_time,
            mime_type=mime_type,
        )

        attach_decorator.additional_properties = d
        return attach_decorator

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
