from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkedDataProof")


@attr.s(auto_attribs=True)
class LinkedDataProof:
    """ """

    created: str
    proof_purpose: str
    type: str
    verification_method: str
    challenge: Union[Unset, str] = UNSET
    domain: Union[Unset, str] = UNSET
    jws: Union[Unset, str] = UNSET
    nonce: Union[Unset, str] = UNSET
    proof_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created = self.created
        proof_purpose = self.proof_purpose
        type = self.type
        verification_method = self.verification_method
        challenge = self.challenge
        domain = self.domain
        jws = self.jws
        nonce = self.nonce
        proof_value = self.proof_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created": created,
                "proofPurpose": proof_purpose,
                "type": type,
                "verificationMethod": verification_method,
            }
        )
        if challenge is not UNSET:
            field_dict["challenge"] = challenge
        if domain is not UNSET:
            field_dict["domain"] = domain
        if jws is not UNSET:
            field_dict["jws"] = jws
        if nonce is not UNSET:
            field_dict["nonce"] = nonce
        if proof_value is not UNSET:
            field_dict["proofValue"] = proof_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created = d.pop("created")

        proof_purpose = d.pop("proofPurpose")

        type = d.pop("type")

        verification_method = d.pop("verificationMethod")

        challenge = d.pop("challenge", UNSET)

        domain = d.pop("domain", UNSET)

        jws = d.pop("jws", UNSET)

        nonce = d.pop("nonce", UNSET)

        proof_value = d.pop("proofValue", UNSET)

        linked_data_proof = cls(
            created=created,
            proof_purpose=proof_purpose,
            type=type,
            verification_method=verification_method,
            challenge=challenge,
            domain=domain,
            jws=jws,
            nonce=nonce,
            proof_value=proof_value,
        )

        linked_data_proof.additional_properties = d
        return linked_data_proof

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
