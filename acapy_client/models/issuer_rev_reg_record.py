from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.indy_rev_reg_def import IndyRevRegDef
from ..models.indy_rev_reg_entry import IndyRevRegEntry
from ..models.issuer_rev_reg_record_revoc_def_type import IssuerRevRegRecordRevocDefType
from ..types import UNSET, Unset

T = TypeVar("T", bound="IssuerRevRegRecord")


@attr.s(auto_attribs=True)
class IssuerRevRegRecord:
    """
    Attributes:
        created_at (Union[Unset, str]): Time of record creation Example: 2021-12-31 23:59:59+00:00.
        cred_def_id (Union[Unset, str]): Credential definition identifier Example: WgWxqztrNooG92RXvxSTWv:3:CL:20:tag.
        error_msg (Union[Unset, str]): Error message Example: Revocation registry undefined.
        issuer_did (Union[Unset, str]): Issuer DID Example: WgWxqztrNooG92RXvxSTWv.
        max_cred_num (Union[Unset, int]): Maximum number of credentials for revocation registry Example: 1000.
        pending_pub (Union[Unset, List[str]]): Credential revocation identifier for credential revoked and pending
            publication to ledger
        record_id (Union[Unset, str]): Issuer revocation registry record identifier Example:
            3fa85f64-5717-4562-b3fc-2c963f66afa6.
        revoc_def_type (Union[Unset, IssuerRevRegRecordRevocDefType]): Revocation registry type (specify CL_ACCUM)
            Example: CL_ACCUM.
        revoc_reg_def (Union[Unset, IndyRevRegDef]):
        revoc_reg_entry (Union[Unset, IndyRevRegEntry]):
        revoc_reg_id (Union[Unset, str]): Revocation registry identifier Example:
            WgWxqztrNooG92RXvxSTWv:4:WgWxqztrNooG92RXvxSTWv:3:CL:20:tag:CL_ACCUM:0.
        state (Union[Unset, str]): Issue revocation registry record state Example: active.
        tag (Union[Unset, str]): Tag within issuer revocation registry identifier
        tails_hash (Union[Unset, str]): Tails hash Example: H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV.
        tails_local_path (Union[Unset, str]): Local path to tails file
        tails_public_uri (Union[Unset, str]): Public URI for tails file
        updated_at (Union[Unset, str]): Time of last record update Example: 2021-12-31 23:59:59+00:00.
    """

    created_at: Union[Unset, str] = UNSET
    cred_def_id: Union[Unset, str] = UNSET
    error_msg: Union[Unset, str] = UNSET
    issuer_did: Union[Unset, str] = UNSET
    max_cred_num: Union[Unset, int] = UNSET
    pending_pub: Union[Unset, List[str]] = UNSET
    record_id: Union[Unset, str] = UNSET
    revoc_def_type: Union[Unset, IssuerRevRegRecordRevocDefType] = UNSET
    revoc_reg_def: Union[Unset, IndyRevRegDef] = UNSET
    revoc_reg_entry: Union[Unset, IndyRevRegEntry] = UNSET
    revoc_reg_id: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    tag: Union[Unset, str] = UNSET
    tails_hash: Union[Unset, str] = UNSET
    tails_local_path: Union[Unset, str] = UNSET
    tails_public_uri: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at
        cred_def_id = self.cred_def_id
        error_msg = self.error_msg
        issuer_did = self.issuer_did
        max_cred_num = self.max_cred_num
        pending_pub: Union[Unset, List[str]] = UNSET
        if not isinstance(self.pending_pub, Unset):
            pending_pub = self.pending_pub

        record_id = self.record_id
        revoc_def_type: Union[Unset, str] = UNSET
        if not isinstance(self.revoc_def_type, Unset):
            revoc_def_type = self.revoc_def_type.value

        revoc_reg_def: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.revoc_reg_def, Unset):
            revoc_reg_def = self.revoc_reg_def.to_dict()

        revoc_reg_entry: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.revoc_reg_entry, Unset):
            revoc_reg_entry = self.revoc_reg_entry.to_dict()

        revoc_reg_id = self.revoc_reg_id
        state = self.state
        tag = self.tag
        tails_hash = self.tails_hash
        tails_local_path = self.tails_local_path
        tails_public_uri = self.tails_public_uri
        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if cred_def_id is not UNSET:
            field_dict["cred_def_id"] = cred_def_id
        if error_msg is not UNSET:
            field_dict["error_msg"] = error_msg
        if issuer_did is not UNSET:
            field_dict["issuer_did"] = issuer_did
        if max_cred_num is not UNSET:
            field_dict["max_cred_num"] = max_cred_num
        if pending_pub is not UNSET:
            field_dict["pending_pub"] = pending_pub
        if record_id is not UNSET:
            field_dict["record_id"] = record_id
        if revoc_def_type is not UNSET:
            field_dict["revoc_def_type"] = revoc_def_type
        if revoc_reg_def is not UNSET:
            field_dict["revoc_reg_def"] = revoc_reg_def
        if revoc_reg_entry is not UNSET:
            field_dict["revoc_reg_entry"] = revoc_reg_entry
        if revoc_reg_id is not UNSET:
            field_dict["revoc_reg_id"] = revoc_reg_id
        if state is not UNSET:
            field_dict["state"] = state
        if tag is not UNSET:
            field_dict["tag"] = tag
        if tails_hash is not UNSET:
            field_dict["tails_hash"] = tails_hash
        if tails_local_path is not UNSET:
            field_dict["tails_local_path"] = tails_local_path
        if tails_public_uri is not UNSET:
            field_dict["tails_public_uri"] = tails_public_uri
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("created_at", UNSET)

        cred_def_id = d.pop("cred_def_id", UNSET)

        error_msg = d.pop("error_msg", UNSET)

        issuer_did = d.pop("issuer_did", UNSET)

        max_cred_num = d.pop("max_cred_num", UNSET)

        pending_pub = cast(List[str], d.pop("pending_pub", UNSET))

        record_id = d.pop("record_id", UNSET)

        _revoc_def_type = d.pop("revoc_def_type", UNSET)
        revoc_def_type: Union[Unset, IssuerRevRegRecordRevocDefType]
        if isinstance(_revoc_def_type, Unset):
            revoc_def_type = UNSET
        else:
            revoc_def_type = IssuerRevRegRecordRevocDefType(_revoc_def_type)

        _revoc_reg_def = d.pop("revoc_reg_def", UNSET)
        revoc_reg_def: Union[Unset, IndyRevRegDef]
        if isinstance(_revoc_reg_def, Unset):
            revoc_reg_def = UNSET
        else:
            revoc_reg_def = IndyRevRegDef.from_dict(_revoc_reg_def)

        _revoc_reg_entry = d.pop("revoc_reg_entry", UNSET)
        revoc_reg_entry: Union[Unset, IndyRevRegEntry]
        if isinstance(_revoc_reg_entry, Unset):
            revoc_reg_entry = UNSET
        else:
            revoc_reg_entry = IndyRevRegEntry.from_dict(_revoc_reg_entry)

        revoc_reg_id = d.pop("revoc_reg_id", UNSET)

        state = d.pop("state", UNSET)

        tag = d.pop("tag", UNSET)

        tails_hash = d.pop("tails_hash", UNSET)

        tails_local_path = d.pop("tails_local_path", UNSET)

        tails_public_uri = d.pop("tails_public_uri", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        issuer_rev_reg_record = cls(
            created_at=created_at,
            cred_def_id=cred_def_id,
            error_msg=error_msg,
            issuer_did=issuer_did,
            max_cred_num=max_cred_num,
            pending_pub=pending_pub,
            record_id=record_id,
            revoc_def_type=revoc_def_type,
            revoc_reg_def=revoc_reg_def,
            revoc_reg_entry=revoc_reg_entry,
            revoc_reg_id=revoc_reg_id,
            state=state,
            tag=tag,
            tails_hash=tails_hash,
            tails_local_path=tails_local_path,
            tails_public_uri=tails_public_uri,
            updated_at=updated_at,
        )

        issuer_rev_reg_record.additional_properties = d
        return issuer_rev_reg_record

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
