from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="V20CredExRecordLDProof")


@attr.s(auto_attribs=True)
class V20CredExRecordLDProof:
    """
    Attributes:
        created_at (Union[Unset, str]): Time of record creation Example: 2021-12-31 23:59:59+00:00.
        cred_ex_id (Union[Unset, str]): Corresponding v2.0 credential exchange record identifier Example:
            3fa85f64-5717-4562-b3fc-2c963f66afa6.
        cred_ex_ld_proof_id (Union[Unset, str]): Record identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        cred_id_stored (Union[Unset, str]): Credential identifier stored in wallet Example:
            3fa85f64-5717-4562-b3fc-2c963f66afa6.
        state (Union[Unset, str]): Current record state Example: active.
        updated_at (Union[Unset, str]): Time of last record update Example: 2021-12-31 23:59:59+00:00.
    """

    created_at: Union[Unset, str] = UNSET
    cred_ex_id: Union[Unset, str] = UNSET
    cred_ex_ld_proof_id: Union[Unset, str] = UNSET
    cred_id_stored: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at
        cred_ex_id = self.cred_ex_id
        cred_ex_ld_proof_id = self.cred_ex_ld_proof_id
        cred_id_stored = self.cred_id_stored
        state = self.state
        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if cred_ex_id is not UNSET:
            field_dict["cred_ex_id"] = cred_ex_id
        if cred_ex_ld_proof_id is not UNSET:
            field_dict["cred_ex_ld_proof_id"] = cred_ex_ld_proof_id
        if cred_id_stored is not UNSET:
            field_dict["cred_id_stored"] = cred_id_stored
        if state is not UNSET:
            field_dict["state"] = state
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("created_at", UNSET)

        cred_ex_id = d.pop("cred_ex_id", UNSET)

        cred_ex_ld_proof_id = d.pop("cred_ex_ld_proof_id", UNSET)

        cred_id_stored = d.pop("cred_id_stored", UNSET)

        state = d.pop("state", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        v20_cred_ex_record_ld_proof = cls(
            created_at=created_at,
            cred_ex_id=cred_ex_id,
            cred_ex_ld_proof_id=cred_ex_ld_proof_id,
            cred_id_stored=cred_id_stored,
            state=state,
            updated_at=updated_at,
        )

        v20_cred_ex_record_ld_proof.additional_properties = d
        return v20_cred_ex_record_ld_proof

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
