from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_pres_preview import IndyPresPreview
from ..types import UNSET, Unset

T = TypeVar("T", bound="PresentationProposal")


@attr.s(auto_attribs=True)
class PresentationProposal:
    """
    Attributes:
        presentation_proposal (IndyPresPreview):
        id (Union[Unset, str]): Message identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        type (Union[Unset, str]): Message type Example: https://didcomm.org/my-family/1.0/my-message-type.
        comment (Union[Unset, None, str]): Human-readable comment
    """

    presentation_proposal: IndyPresPreview
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    comment: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        presentation_proposal = self.presentation_proposal.to_dict()

        id = self.id
        type = self.type
        comment = self.comment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "presentation_proposal": presentation_proposal,
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
        presentation_proposal = IndyPresPreview.from_dict(d.pop("presentation_proposal"))

        id = d.pop("@id", UNSET)

        type = d.pop("@type", UNSET)

        comment = d.pop("comment", UNSET)

        presentation_proposal = cls(
            presentation_proposal=presentation_proposal,
            id=id,
            type=type,
            comment=comment,
        )

        presentation_proposal.additional_properties = d
        return presentation_proposal

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
