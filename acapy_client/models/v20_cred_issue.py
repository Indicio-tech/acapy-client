from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attach_decorator import AttachDecorator
from ..models.v20_cred_format import V20CredFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20CredIssue")


@attr.s(auto_attribs=True)
class V20CredIssue:
    """
    Attributes:
        credentialsattach (List[AttachDecorator]): Credential attachments
        formats (List[V20CredFormat]): Acceptable attachment formats
        id (Union[Unset, str]): Message identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        type (Union[Unset, str]): Message type Example: https://didcomm.org/my-family/1.0/my-message-type.
        comment (Union[Unset, None, str]): Human-readable comment
        replacement_id (Union[Unset, str]): Issuer-unique identifier to coordinate credential replacement Example:
            3fa85f64-5717-4562-b3fc-2c963f66afa6.
    """

    credentialsattach: List[AttachDecorator]
    formats: List[V20CredFormat]
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    comment: Union[Unset, None, str] = UNSET
    replacement_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credentialsattach = []
        for credentialsattach_item_data in self.credentialsattach:
            credentialsattach_item = credentialsattach_item_data.to_dict()

            credentialsattach.append(credentialsattach_item)

        formats = []
        for formats_item_data in self.formats:
            formats_item = formats_item_data.to_dict()

            formats.append(formats_item)

        id = self.id
        type = self.type
        comment = self.comment
        replacement_id = self.replacement_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credentials~attach": credentialsattach,
                "formats": formats,
            }
        )
        if id is not UNSET:
            field_dict["@id"] = id
        if type is not UNSET:
            field_dict["@type"] = type
        if comment is not UNSET:
            field_dict["comment"] = comment
        if replacement_id is not UNSET:
            field_dict["replacement_id"] = replacement_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credentialsattach = []
        _credentialsattach = d.pop("credentials~attach")
        for credentialsattach_item_data in _credentialsattach:
            credentialsattach_item = AttachDecorator.from_dict(credentialsattach_item_data)

            credentialsattach.append(credentialsattach_item)

        formats = []
        _formats = d.pop("formats")
        for formats_item_data in _formats:
            formats_item = V20CredFormat.from_dict(formats_item_data)

            formats.append(formats_item)

        id = d.pop("@id", UNSET)

        type = d.pop("@type", UNSET)

        comment = d.pop("comment", UNSET)

        replacement_id = d.pop("replacement_id", UNSET)

        v20_cred_issue = cls(
            credentialsattach=credentialsattach,
            formats=formats,
            id=id,
            type=type,
            comment=comment,
            replacement_id=replacement_id,
        )

        v20_cred_issue.additional_properties = d
        return v20_cred_issue

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
