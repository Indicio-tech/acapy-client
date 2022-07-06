from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.revoke_request_notify_version import RevokeRequestNotifyVersion
from ..types import UNSET, Unset

T = TypeVar("T", bound="RevokeRequest")


@attr.s(auto_attribs=True)
class RevokeRequest:
    """
    Attributes:
        comment (Union[Unset, str]): Optional comment to include in revocation notification
        connection_id (Union[Unset, str]): Connection ID to which the revocation notification will be sent; required if
            notify is true Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        cred_ex_id (Union[Unset, str]): Credential exchange identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        cred_rev_id (Union[Unset, str]): Credential revocation identifier Example: 12345.
        notify (Union[Unset, bool]): Send a notification to the credential recipient
        notify_version (Union[Unset, RevokeRequestNotifyVersion]): Specify which version of the revocation notification
            should be sent
        publish (Union[Unset, bool]): (True) publish revocation to ledger immediately, or (default, False) mark it
            pending
        rev_reg_id (Union[Unset, str]): Revocation registry identifier Example:
            WgWxqztrNooG92RXvxSTWv:4:WgWxqztrNooG92RXvxSTWv:3:CL:20:tag:CL_ACCUM:0.
        thread_id (Union[Unset, str]): Thread ID of the credential exchange message thread resulting in the credential
            now being revoked; required if notify is true
    """

    comment: Union[Unset, str] = UNSET
    connection_id: Union[Unset, str] = UNSET
    cred_ex_id: Union[Unset, str] = UNSET
    cred_rev_id: Union[Unset, str] = UNSET
    notify: Union[Unset, bool] = UNSET
    notify_version: Union[Unset, RevokeRequestNotifyVersion] = UNSET
    publish: Union[Unset, bool] = UNSET
    rev_reg_id: Union[Unset, str] = UNSET
    thread_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comment = self.comment
        connection_id = self.connection_id
        cred_ex_id = self.cred_ex_id
        cred_rev_id = self.cred_rev_id
        notify = self.notify
        notify_version: Union[Unset, str] = UNSET
        if not isinstance(self.notify_version, Unset):
            notify_version = self.notify_version.value

        publish = self.publish
        rev_reg_id = self.rev_reg_id
        thread_id = self.thread_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comment is not UNSET:
            field_dict["comment"] = comment
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if cred_ex_id is not UNSET:
            field_dict["cred_ex_id"] = cred_ex_id
        if cred_rev_id is not UNSET:
            field_dict["cred_rev_id"] = cred_rev_id
        if notify is not UNSET:
            field_dict["notify"] = notify
        if notify_version is not UNSET:
            field_dict["notify_version"] = notify_version
        if publish is not UNSET:
            field_dict["publish"] = publish
        if rev_reg_id is not UNSET:
            field_dict["rev_reg_id"] = rev_reg_id
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        comment = d.pop("comment", UNSET)

        connection_id = d.pop("connection_id", UNSET)

        cred_ex_id = d.pop("cred_ex_id", UNSET)

        cred_rev_id = d.pop("cred_rev_id", UNSET)

        notify = d.pop("notify", UNSET)

        _notify_version = d.pop("notify_version", UNSET)
        notify_version: Union[Unset, RevokeRequestNotifyVersion]
        if isinstance(_notify_version, Unset):
            notify_version = UNSET
        else:
            notify_version = RevokeRequestNotifyVersion(_notify_version)

        publish = d.pop("publish", UNSET)

        rev_reg_id = d.pop("rev_reg_id", UNSET)

        thread_id = d.pop("thread_id", UNSET)

        revoke_request = cls(
            comment=comment,
            connection_id=connection_id,
            cred_ex_id=cred_ex_id,
            cred_rev_id=cred_rev_id,
            notify=notify,
            notify_version=notify_version,
            publish=publish,
            rev_reg_id=rev_reg_id,
            thread_id=thread_id,
        )

        revoke_request.additional_properties = d
        return revoke_request

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
