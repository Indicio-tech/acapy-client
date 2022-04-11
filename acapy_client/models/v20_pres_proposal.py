from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attach_decorator import AttachDecorator
from ..models.v20_pres_format import V20PresFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20PresProposal")


@attr.s(auto_attribs=True)
class V20PresProposal:
    """
    Attributes:
        formats (List[V20PresFormat]):
        proposalsattach (List[AttachDecorator]): Attachment per acceptable format on corresponding identifier
        id (Union[Unset, str]): Message identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        type (Union[Unset, str]): Message type Example: https://didcomm.org/my-family/1.0/my-message-type.
        comment (Union[Unset, str]): Human-readable comment
    """

    formats: List[V20PresFormat]
    proposalsattach: List[AttachDecorator]
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    comment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        formats = []
        for formats_item_data in self.formats:
            formats_item = formats_item_data.to_dict()

            formats.append(formats_item)

        proposalsattach = []
        for proposalsattach_item_data in self.proposalsattach:
            proposalsattach_item = proposalsattach_item_data.to_dict()

            proposalsattach.append(proposalsattach_item)

        id = self.id
        type = self.type
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "formats": formats,
                "proposals~attach": proposalsattach,
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
            formats_item = V20PresFormat.from_dict(formats_item_data)

            formats.append(formats_item)

        proposalsattach = []
        _proposalsattach = d.pop("proposals~attach")
        for proposalsattach_item_data in _proposalsattach:
            proposalsattach_item = AttachDecorator.from_dict(proposalsattach_item_data)

            proposalsattach.append(proposalsattach_item)

        id = d.pop("@id", UNSET)

        type = d.pop("@type", UNSET)

        comment = d.pop("comment", UNSET)

        v20_pres_proposal = cls(
            formats=formats,
            proposalsattach=proposalsattach,
            id=id,
            type=type,
            comment=comment,
        )

        v20_pres_proposal.additional_properties = d
        return v20_pres_proposal

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
