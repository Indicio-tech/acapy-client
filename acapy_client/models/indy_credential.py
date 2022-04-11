from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_credential_rev_reg import IndyCredentialRevReg
from ..models.indy_credential_signature import IndyCredentialSignature
from ..models.indy_credential_signature_correctness_proof import IndyCredentialSignatureCorrectnessProof
from ..models.indy_credential_values import IndyCredentialValues
from ..models.indy_credential_witness import IndyCredentialWitness
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyCredential")


@attr.s(auto_attribs=True)
class IndyCredential:
    """
    Attributes:
        cred_def_id (str): Credential definition identifier Example: WgWxqztrNooG92RXvxSTWv:3:CL:20:tag.
        schema_id (str): Schema identifier Example: WgWxqztrNooG92RXvxSTWv:2:schema_name:1.0.
        signature (IndyCredentialSignature): Credential signature
        signature_correctness_proof (IndyCredentialSignatureCorrectnessProof): Credential signature correctness proof
        values (IndyCredentialValues): Credential attributes
        rev_reg (Union[Unset, None, IndyCredentialRevReg]): Revocation registry state
        rev_reg_id (Union[Unset, None, str]): Revocation registry identifier Example:
            WgWxqztrNooG92RXvxSTWv:4:WgWxqztrNooG92RXvxSTWv:3:CL:20:tag:CL_ACCUM:0.
        witness (Union[Unset, None, IndyCredentialWitness]): Witness for revocation proof
    """

    cred_def_id: str
    schema_id: str
    signature: IndyCredentialSignature
    signature_correctness_proof: IndyCredentialSignatureCorrectnessProof
    values: IndyCredentialValues
    rev_reg: Union[Unset, None, IndyCredentialRevReg] = UNSET
    rev_reg_id: Union[Unset, None, str] = UNSET
    witness: Union[Unset, None, IndyCredentialWitness] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cred_def_id = self.cred_def_id
        schema_id = self.schema_id
        signature = self.signature.to_dict()

        signature_correctness_proof = self.signature_correctness_proof.to_dict()

        values = self.values.to_dict()

        rev_reg: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.rev_reg, Unset):
            rev_reg = self.rev_reg.to_dict() if self.rev_reg else None

        rev_reg_id = self.rev_reg_id
        witness: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.witness, Unset):
            witness = self.witness.to_dict() if self.witness else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cred_def_id": cred_def_id,
                "schema_id": schema_id,
                "signature": signature,
                "signature_correctness_proof": signature_correctness_proof,
                "values": values,
            }
        )
        if rev_reg is not UNSET:
            field_dict["rev_reg"] = rev_reg
        if rev_reg_id is not UNSET:
            field_dict["rev_reg_id"] = rev_reg_id
        if witness is not UNSET:
            field_dict["witness"] = witness

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cred_def_id = d.pop("cred_def_id")

        schema_id = d.pop("schema_id")

        signature = IndyCredentialSignature.from_dict(d.pop("signature"))

        signature_correctness_proof = IndyCredentialSignatureCorrectnessProof.from_dict(
            d.pop("signature_correctness_proof")
        )

        values = IndyCredentialValues.from_dict(d.pop("values"))

        _rev_reg = d.pop("rev_reg", UNSET)
        rev_reg: Union[Unset, None, IndyCredentialRevReg]
        if _rev_reg is None:
            rev_reg = None
        elif isinstance(_rev_reg, Unset):
            rev_reg = UNSET
        else:
            rev_reg = IndyCredentialRevReg.from_dict(_rev_reg)

        rev_reg_id = d.pop("rev_reg_id", UNSET)

        _witness = d.pop("witness", UNSET)
        witness: Union[Unset, None, IndyCredentialWitness]
        if _witness is None:
            witness = None
        elif isinstance(_witness, Unset):
            witness = UNSET
        else:
            witness = IndyCredentialWitness.from_dict(_witness)

        indy_credential = cls(
            cred_def_id=cred_def_id,
            schema_id=schema_id,
            signature=signature,
            signature_correctness_proof=signature_correctness_proof,
            values=values,
            rev_reg=rev_reg,
            rev_reg_id=rev_reg_id,
            witness=witness,
        )

        indy_credential.additional_properties = d
        return indy_credential

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
