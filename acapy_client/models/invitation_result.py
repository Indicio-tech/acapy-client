from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.connection_invitation import ConnectionInvitation
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvitationResult")


@attr.s(auto_attribs=True)
class InvitationResult:
    """
    Attributes:
        connection_id (Union[Unset, str]): Connection identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        invitation (Union[Unset, ConnectionInvitation]):
        invitation_url (Union[Unset, str]): Invitation URL Example:
            http://192.168.56.101:8020/invite?c_i=eyJAdHlwZSI6Li4ufQ==.
    """

    connection_id: Union[Unset, str] = UNSET
    invitation: Union[Unset, ConnectionInvitation] = UNSET
    invitation_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id
        invitation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.invitation, Unset):
            invitation = self.invitation.to_dict()

        invitation_url = self.invitation_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if invitation is not UNSET:
            field_dict["invitation"] = invitation
        if invitation_url is not UNSET:
            field_dict["invitation_url"] = invitation_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connection_id", UNSET)

        _invitation = d.pop("invitation", UNSET)
        invitation: Union[Unset, ConnectionInvitation]
        if isinstance(_invitation, Unset):
            invitation = UNSET
        else:
            invitation = ConnectionInvitation.from_dict(_invitation)

        invitation_url = d.pop("invitation_url", UNSET)

        invitation_result = cls(
            connection_id=connection_id,
            invitation=invitation,
            invitation_url=invitation_url,
        )

        invitation_result.additional_properties = d
        return invitation_result

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
