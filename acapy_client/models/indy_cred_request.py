from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_cred_request_blinded_ms import IndyCredRequestBlindedMs
from ..models.indy_cred_request_blinded_ms_correctness_proof import IndyCredRequestBlindedMsCorrectnessProof
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyCredRequest")


@attr.s(auto_attribs=True)
class IndyCredRequest:
    """
    Attributes:
        blinded_ms (IndyCredRequestBlindedMs): Blinded master secret
        blinded_ms_correctness_proof (IndyCredRequestBlindedMsCorrectnessProof): Blinded master secret correctness proof
        cred_def_id (str): Credential definition identifier Example: WgWxqztrNooG92RXvxSTWv:3:CL:20:tag.
        nonce (str): Nonce in credential request Example: 0.
        prover_did (Union[Unset, str]): Prover DID Example: WgWxqztrNooG92RXvxSTWv.
    """

    blinded_ms: IndyCredRequestBlindedMs
    blinded_ms_correctness_proof: IndyCredRequestBlindedMsCorrectnessProof
    cred_def_id: str
    nonce: str
    prover_did: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        blinded_ms = self.blinded_ms.to_dict()

        blinded_ms_correctness_proof = self.blinded_ms_correctness_proof.to_dict()

        cred_def_id = self.cred_def_id
        nonce = self.nonce
        prover_did = self.prover_did

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "blinded_ms": blinded_ms,
                "blinded_ms_correctness_proof": blinded_ms_correctness_proof,
                "cred_def_id": cred_def_id,
                "nonce": nonce,
            }
        )
        if prover_did is not UNSET:
            field_dict["prover_did"] = prover_did

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        blinded_ms = IndyCredRequestBlindedMs.from_dict(d.pop("blinded_ms"))

        blinded_ms_correctness_proof = IndyCredRequestBlindedMsCorrectnessProof.from_dict(
            d.pop("blinded_ms_correctness_proof")
        )

        cred_def_id = d.pop("cred_def_id")

        nonce = d.pop("nonce")

        prover_did = d.pop("prover_did", UNSET)

        indy_cred_request = cls(
            blinded_ms=blinded_ms,
            blinded_ms_correctness_proof=blinded_ms_correctness_proof,
            cred_def_id=cred_def_id,
            nonce=nonce,
            prover_did=prover_did,
        )

        indy_cred_request.additional_properties = d
        return indy_cred_request

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
