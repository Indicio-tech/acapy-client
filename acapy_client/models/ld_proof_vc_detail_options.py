from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.credential_status_options import CredentialStatusOptions
from ..types import UNSET, Unset

T = TypeVar("T", bound="LDProofVCDetailOptions")


@attr.s(auto_attribs=True)
class LDProofVCDetailOptions:
    """
    Attributes:
        proof_type (str): The proof type used for the proof. Should match suites registered in the Linked Data
            Cryptographic Suite Registry Example: Ed25519Signature2018.
        challenge (Union[Unset, str]): A challenge to include in the proof. SHOULD be provided by the requesting party
            of the credential (=holder) Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        created (Union[Unset, str]): The date and time of the proof (with a maximum accuracy in seconds). Defaults to
            current system time Example: 2021-12-31 23:59:59+00:00.
        credential_status (Union[Unset, CredentialStatusOptions]):
        domain (Union[Unset, str]): The intended domain of validity for the proof Example: example.com.
        proof_purpose (Union[Unset, str]): The proof purpose used for the proof. Should match proof purposes registered
            in the Linked Data Proofs Specification Example: assertionMethod.
    """

    proof_type: str
    challenge: Union[Unset, str] = UNSET
    created: Union[Unset, str] = UNSET
    credential_status: Union[Unset, CredentialStatusOptions] = UNSET
    domain: Union[Unset, str] = UNSET
    proof_purpose: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        proof_type = self.proof_type
        challenge = self.challenge
        created = self.created
        credential_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_status, Unset):
            credential_status = self.credential_status.to_dict()

        domain = self.domain
        proof_purpose = self.proof_purpose

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proofType": proof_type,
            }
        )
        if challenge is not UNSET:
            field_dict["challenge"] = challenge
        if created is not UNSET:
            field_dict["created"] = created
        if credential_status is not UNSET:
            field_dict["credentialStatus"] = credential_status
        if domain is not UNSET:
            field_dict["domain"] = domain
        if proof_purpose is not UNSET:
            field_dict["proofPurpose"] = proof_purpose

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        proof_type = d.pop("proofType")

        challenge = d.pop("challenge", UNSET)

        created = d.pop("created", UNSET)

        _credential_status = d.pop("credentialStatus", UNSET)
        credential_status: Union[Unset, CredentialStatusOptions]
        if isinstance(_credential_status, Unset):
            credential_status = UNSET
        else:
            credential_status = CredentialStatusOptions.from_dict(_credential_status)

        domain = d.pop("domain", UNSET)

        proof_purpose = d.pop("proofPurpose", UNSET)

        ld_proof_vc_detail_options = cls(
            proof_type=proof_type,
            challenge=challenge,
            created=created,
            credential_status=credential_status,
            domain=domain,
            proof_purpose=proof_purpose,
        )

        ld_proof_vc_detail_options.additional_properties = d
        return ld_proof_vc_detail_options

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
