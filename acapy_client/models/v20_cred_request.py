from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attach_decorator import AttachDecorator
from ..models.v20_cred_format import V20CredFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20CredRequest")


@attr.s(auto_attribs=True)
class V20CredRequest:
    """
    Attributes:
        formats (List[V20CredFormat]): Acceptable attachment formats
        requestsattach (List[AttachDecorator]): Request attachments
        id (Union[Unset, str]): Message identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        type (Union[Unset, str]): Message type Example: https://didcomm.org/my-family/1.0/my-message-type.
        comment (Union[Unset, None, str]): Human-readable comment
    """

    formats: List[V20CredFormat]
    requestsattach: List[AttachDecorator]
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    comment: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        formats = []
        for formats_item_data in self.formats:
            formats_item = formats_item_data.to_dict()

            formats.append(formats_item)

        requestsattach = []
        for requestsattach_item_data in self.requestsattach:
            requestsattach_item = requestsattach_item_data.to_dict()

            requestsattach.append(requestsattach_item)

        id = self.id
        type = self.type
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "formats": formats,
                "requests~attach": requestsattach,
            }
        )
        if id is not UNSET:
            field_dict["@id"] = id
        if type is not UNSET:
            field_dict["@type"] = type
        if comment is not UNSET:
            field_dict["comment"] = comment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        formats = []
        _formats = d.pop("formats")
        for formats_item_data in _formats:
            formats_item = V20CredFormat.from_dict(formats_item_data)

            formats.append(formats_item)

        requestsattach = []
        _requestsattach = d.pop("requests~attach")
        for requestsattach_item_data in _requestsattach:
            requestsattach_item = AttachDecorator.from_dict(requestsattach_item_data)

            requestsattach.append(requestsattach_item)

        id = d.pop("@id", UNSET)

        type = d.pop("@type", UNSET)

        comment = d.pop("comment", UNSET)

        v20_cred_request = cls(
            formats=formats,
            requestsattach=requestsattach,
            id=id,
            type=type,
            comment=comment,
        )

        v20_cred_request.additional_properties = d
        return v20_cred_request

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
