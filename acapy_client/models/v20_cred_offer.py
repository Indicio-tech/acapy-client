from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attach_decorator import AttachDecorator
from ..models.v20_cred_format import V20CredFormat
from ..models.v20_cred_preview import V20CredPreview
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20CredOffer")


@attr.s(auto_attribs=True)
class V20CredOffer:
    """
    Attributes:
        formats (List[V20CredFormat]): Acceptable credential formats
        offersattach (List[AttachDecorator]): Offer attachments
        id (Union[Unset, str]): Message identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        type (Union[Unset, str]): Message type Example: https://didcomm.org/my-family/1.0/my-message-type.
        comment (Union[Unset, None, str]): Human-readable comment
        credential_preview (Union[Unset, V20CredPreview]):
        replacement_id (Union[Unset, str]): Issuer-unique identifier to coordinate credential replacement Example:
            3fa85f64-5717-4562-b3fc-2c963f66afa6.
    """

    formats: List[V20CredFormat]
    offersattach: List[AttachDecorator]
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    comment: Union[Unset, None, str] = UNSET
    credential_preview: Union[Unset, V20CredPreview] = UNSET
    replacement_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        formats = []
        for formats_item_data in self.formats:
            formats_item = formats_item_data.to_dict()

            formats.append(formats_item)

        offersattach = []
        for offersattach_item_data in self.offersattach:
            offersattach_item = offersattach_item_data.to_dict()

            offersattach.append(offersattach_item)

        id = self.id
        type = self.type
        comment = self.comment
        credential_preview: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_preview, Unset):
            credential_preview = self.credential_preview.to_dict()

        replacement_id = self.replacement_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "formats": formats,
                "offers~attach": offersattach,
            }
        )
        if id is not UNSET:
            field_dict["@id"] = id
        if type is not UNSET:
            field_dict["@type"] = type
        if comment is not UNSET:
            field_dict["comment"] = comment
        if credential_preview is not UNSET:
            field_dict["credential_preview"] = credential_preview
        if replacement_id is not UNSET:
            field_dict["replacement_id"] = replacement_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        formats = []
        _formats = d.pop("formats")
        for formats_item_data in _formats:
            formats_item = V20CredFormat.from_dict(formats_item_data)

            formats.append(formats_item)

        offersattach = []
        _offersattach = d.pop("offers~attach")
        for offersattach_item_data in _offersattach:
            offersattach_item = AttachDecorator.from_dict(offersattach_item_data)

            offersattach.append(offersattach_item)

        id = d.pop("@id", UNSET)

        type = d.pop("@type", UNSET)

        comment = d.pop("comment", UNSET)

        _credential_preview = d.pop("credential_preview", UNSET)
        credential_preview: Union[Unset, V20CredPreview]
        if isinstance(_credential_preview, Unset):
            credential_preview = UNSET
        else:
            credential_preview = V20CredPreview.from_dict(_credential_preview)

        replacement_id = d.pop("replacement_id", UNSET)

        v20_cred_offer = cls(
            formats=formats,
            offersattach=offersattach,
            id=id,
            type=type,
            comment=comment,
            credential_preview=credential_preview,
            replacement_id=replacement_id,
        )

        v20_cred_offer.additional_properties = d
        return v20_cred_offer

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
