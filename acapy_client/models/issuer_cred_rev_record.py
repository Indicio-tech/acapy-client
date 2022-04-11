from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssuerCredRevRecord")


@attr.s(auto_attribs=True)
class IssuerCredRevRecord:
    """
    Attributes:
        created_at (Union[Unset, str]): Time of record creation Example: 2021-12-31 23:59:59+00:00.
        cred_def_id (Union[Unset, str]): Credential definition identifier Example: WgWxqztrNooG92RXvxSTWv:3:CL:20:tag.
        cred_ex_id (Union[Unset, str]): Credential exchange record identifier at credential issue Example:
            3fa85f64-5717-4562-b3fc-2c963f66afa6.
        cred_rev_id (Union[Unset, str]): Credential revocation identifier Example: 12345.
        record_id (Union[Unset, str]): Issuer credential revocation record identifier Example:
            3fa85f64-5717-4562-b3fc-2c963f66afa6.
        rev_reg_id (Union[Unset, str]): Revocation registry identifier Example:
            WgWxqztrNooG92RXvxSTWv:4:WgWxqztrNooG92RXvxSTWv:3:CL:20:tag:CL_ACCUM:0.
        state (Union[Unset, str]): Issue credential revocation record state Example: issued.
        updated_at (Union[Unset, str]): Time of last record update Example: 2021-12-31 23:59:59+00:00.
    """

    created_at: Union[Unset, str] = UNSET
    cred_def_id: Union[Unset, str] = UNSET
    cred_ex_id: Union[Unset, str] = UNSET
    cred_rev_id: Union[Unset, str] = UNSET
    record_id: Union[Unset, str] = UNSET
    rev_reg_id: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at
        cred_def_id = self.cred_def_id
        cred_ex_id = self.cred_ex_id
        cred_rev_id = self.cred_rev_id
        record_id = self.record_id
        rev_reg_id = self.rev_reg_id
        state = self.state
        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if cred_def_id is not UNSET:
            field_dict["cred_def_id"] = cred_def_id
        if cred_ex_id is not UNSET:
            field_dict["cred_ex_id"] = cred_ex_id
        if cred_rev_id is not UNSET:
            field_dict["cred_rev_id"] = cred_rev_id
        if record_id is not UNSET:
            field_dict["record_id"] = record_id
        if rev_reg_id is not UNSET:
            field_dict["rev_reg_id"] = rev_reg_id
        if state is not UNSET:
            field_dict["state"] = state
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("created_at", UNSET)

        cred_def_id = d.pop("cred_def_id", UNSET)

        cred_ex_id = d.pop("cred_ex_id", UNSET)

        cred_rev_id = d.pop("cred_rev_id", UNSET)

        record_id = d.pop("record_id", UNSET)

        rev_reg_id = d.pop("rev_reg_id", UNSET)

        state = d.pop("state", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        issuer_cred_rev_record = cls(
            created_at=created_at,
            cred_def_id=cred_def_id,
            cred_ex_id=cred_ex_id,
            cred_rev_id=cred_rev_id,
            record_id=record_id,
            rev_reg_id=rev_reg_id,
            state=state,
            updated_at=updated_at,
        )

        issuer_cred_rev_record.additional_properties = d
        return issuer_cred_rev_record

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
