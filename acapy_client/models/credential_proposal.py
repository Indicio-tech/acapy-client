from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.credential_preview import CredentialPreview
from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialProposal")


@attr.s(auto_attribs=True)
class CredentialProposal:
    """
    Attributes:
        id (Union[Unset, str]): Message identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        type (Union[Unset, str]): Message type Example: https://didcomm.org/my-family/1.0/my-message-type.
        comment (Union[Unset, None, str]): Human-readable comment
        cred_def_id (Union[Unset, str]):  Example: WgWxqztrNooG92RXvxSTWv:3:CL:20:tag.
        credential_proposal (Union[Unset, CredentialPreview]):
        issuer_did (Union[Unset, str]):  Example: WgWxqztrNooG92RXvxSTWv.
        schema_id (Union[Unset, str]):  Example: WgWxqztrNooG92RXvxSTWv:2:schema_name:1.0.
        schema_issuer_did (Union[Unset, str]):  Example: WgWxqztrNooG92RXvxSTWv.
        schema_name (Union[Unset, str]):
        schema_version (Union[Unset, str]):  Example: 1.0.
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    comment: Union[Unset, None, str] = UNSET
    cred_def_id: Union[Unset, str] = UNSET
    credential_proposal: Union[Unset, CredentialPreview] = UNSET
    issuer_did: Union[Unset, str] = UNSET
    schema_id: Union[Unset, str] = UNSET
    schema_issuer_did: Union[Unset, str] = UNSET
    schema_name: Union[Unset, str] = UNSET
    schema_version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        comment = self.comment
        cred_def_id = self.cred_def_id
        credential_proposal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_proposal, Unset):
            credential_proposal = self.credential_proposal.to_dict()

        issuer_did = self.issuer_did
        schema_id = self.schema_id
        schema_issuer_did = self.schema_issuer_did
        schema_name = self.schema_name
        schema_version = self.schema_version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["@id"] = id
        if type is not UNSET:
            field_dict["@type"] = type
        if comment is not UNSET:
            field_dict["comment"] = comment
        if cred_def_id is not UNSET:
            field_dict["cred_def_id"] = cred_def_id
        if credential_proposal is not UNSET:
            field_dict["credential_proposal"] = credential_proposal
        if issuer_did is not UNSET:
            field_dict["issuer_did"] = issuer_did
        if schema_id is not UNSET:
            field_dict["schema_id"] = schema_id
        if schema_issuer_did is not UNSET:
            field_dict["schema_issuer_did"] = schema_issuer_did
        if schema_name is not UNSET:
            field_dict["schema_name"] = schema_name
        if schema_version is not UNSET:
            field_dict["schema_version"] = schema_version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("@id", UNSET)

        type = d.pop("@type", UNSET)

        comment = d.pop("comment", UNSET)

        cred_def_id = d.pop("cred_def_id", UNSET)

        _credential_proposal = d.pop("credential_proposal", UNSET)
        credential_proposal: Union[Unset, CredentialPreview]
        if isinstance(_credential_proposal, Unset):
            credential_proposal = UNSET
        else:
            credential_proposal = CredentialPreview.from_dict(_credential_proposal)

        issuer_did = d.pop("issuer_did", UNSET)

        schema_id = d.pop("schema_id", UNSET)

        schema_issuer_did = d.pop("schema_issuer_did", UNSET)

        schema_name = d.pop("schema_name", UNSET)

        schema_version = d.pop("schema_version", UNSET)

        credential_proposal = cls(
            id=id,
            type=type,
            comment=comment,
            cred_def_id=cred_def_id,
            credential_proposal=credential_proposal,
            issuer_did=issuer_did,
            schema_id=schema_id,
            schema_issuer_did=schema_issuer_did,
            schema_name=schema_name,
            schema_version=schema_version,
        )

        credential_proposal.additional_properties = d
        return credential_proposal

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
