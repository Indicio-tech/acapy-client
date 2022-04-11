from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyProofIdentifier")


@attr.s(auto_attribs=True)
class IndyProofIdentifier:
    """
    Attributes:
        cred_def_id (Union[Unset, str]): Credential definition identifier Example: WgWxqztrNooG92RXvxSTWv:3:CL:20:tag.
        rev_reg_id (Union[Unset, None, str]): Revocation registry identifier Example:
            WgWxqztrNooG92RXvxSTWv:4:WgWxqztrNooG92RXvxSTWv:3:CL:20:tag:CL_ACCUM:0.
        schema_id (Union[Unset, str]): Schema identifier Example: WgWxqztrNooG92RXvxSTWv:2:schema_name:1.0.
        timestamp (Union[Unset, None, int]): Timestamp epoch Example: 1640995199.
    """

    cred_def_id: Union[Unset, str] = UNSET
    rev_reg_id: Union[Unset, None, str] = UNSET
    schema_id: Union[Unset, str] = UNSET
    timestamp: Union[Unset, None, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cred_def_id = self.cred_def_id
        rev_reg_id = self.rev_reg_id
        schema_id = self.schema_id
        timestamp = self.timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cred_def_id is not UNSET:
            field_dict["cred_def_id"] = cred_def_id
        if rev_reg_id is not UNSET:
            field_dict["rev_reg_id"] = rev_reg_id
        if schema_id is not UNSET:
            field_dict["schema_id"] = schema_id
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cred_def_id = d.pop("cred_def_id", UNSET)

        rev_reg_id = d.pop("rev_reg_id", UNSET)

        schema_id = d.pop("schema_id", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        indy_proof_identifier = cls(
            cred_def_id=cred_def_id,
            rev_reg_id=rev_reg_id,
            schema_id=schema_id,
            timestamp=timestamp,
        )

        indy_proof_identifier.additional_properties = d
        return indy_proof_identifier

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
