from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.invitation_message import InvitationMessage
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvitationRecord")


@attr.s(auto_attribs=True)
class InvitationRecord:
    """
    Attributes:
        created_at (Union[Unset, str]): Time of record creation Example: 2021-12-31 23:59:59+00:00.
        invi_msg_id (Union[Unset, str]): Invitation message identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        invitation (Union[Unset, InvitationMessage]):
        invitation_id (Union[Unset, str]): Invitation record identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        invitation_url (Union[Unset, str]): Invitation message URL Example:
            https://example.com/endpoint?c_i=eyJAdHlwZSI6ICIuLi4iLCAiLi4uIjogIi4uLiJ9XX0=.
        oob_id (Union[Unset, str]): Out of band record identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        state (Union[Unset, str]): Out of band message exchange state Example: await_response.
        trace (Union[Unset, bool]): Record trace information, based on agent configuration
        updated_at (Union[Unset, str]): Time of last record update Example: 2021-12-31 23:59:59+00:00.
    """

    created_at: Union[Unset, str] = UNSET
    invi_msg_id: Union[Unset, str] = UNSET
    invitation: Union[Unset, InvitationMessage] = UNSET
    invitation_id: Union[Unset, str] = UNSET
    invitation_url: Union[Unset, str] = UNSET
    oob_id: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    trace: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at
        invi_msg_id = self.invi_msg_id
        invitation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invitation, Unset):
            invitation = self.invitation.to_dict()

        invitation_id = self.invitation_id
        invitation_url = self.invitation_url
        oob_id = self.oob_id
        state = self.state
        trace = self.trace
        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if invi_msg_id is not UNSET:
            field_dict["invi_msg_id"] = invi_msg_id
        if invitation is not UNSET:
            field_dict["invitation"] = invitation
        if invitation_id is not UNSET:
            field_dict["invitation_id"] = invitation_id
        if invitation_url is not UNSET:
            field_dict["invitation_url"] = invitation_url
        if oob_id is not UNSET:
            field_dict["oob_id"] = oob_id
        if state is not UNSET:
            field_dict["state"] = state
        if trace is not UNSET:
            field_dict["trace"] = trace
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("created_at", UNSET)

        invi_msg_id = d.pop("invi_msg_id", UNSET)

        _invitation = d.pop("invitation", UNSET)
        invitation: Union[Unset, InvitationMessage]
        if isinstance(_invitation, Unset):
            invitation = UNSET
        else:
            invitation = InvitationMessage.from_dict(_invitation)

        invitation_id = d.pop("invitation_id", UNSET)

        invitation_url = d.pop("invitation_url", UNSET)

        oob_id = d.pop("oob_id", UNSET)

        state = d.pop("state", UNSET)

        trace = d.pop("trace", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        invitation_record = cls(
            created_at=created_at,
            invi_msg_id=invi_msg_id,
            invitation=invitation,
            invitation_id=invitation_id,
            invitation_url=invitation_url,
            oob_id=oob_id,
            state=state,
            trace=trace,
            updated_at=updated_at,
        )

        invitation_record.additional_properties = d
        return invitation_record

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
