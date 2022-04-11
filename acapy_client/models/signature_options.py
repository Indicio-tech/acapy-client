from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SignatureOptions")


@attr.s(auto_attribs=True)
class SignatureOptions:
    """
    Attributes:
        proof_purpose (str):
        verification_method (str):
        challenge (Union[Unset, str]):
        domain (Union[Unset, str]):
        type (Union[Unset, str]):
    """

    proof_purpose: str
    verification_method: str
    challenge: Union[Unset, str] = UNSET
    domain: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        proof_purpose = self.proof_purpose
        verification_method = self.verification_method
        challenge = self.challenge
        domain = self.domain
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "proofPurpose": proof_purpose,
                "verificationMethod": verification_method,
            }
        )
        if challenge is not UNSET:
            field_dict["challenge"] = challenge
        if domain is not UNSET:
            field_dict["domain"] = domain
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        proof_purpose = d.pop("proofPurpose")

        verification_method = d.pop("verificationMethod")

        challenge = d.pop("challenge", UNSET)

        domain = d.pop("domain", UNSET)

        type = d.pop("type", UNSET)

        signature_options = cls(
            proof_purpose=proof_purpose,
            verification_method=verification_method,
            challenge=challenge,
            domain=domain,
            type=type,
        )

        signature_options.additional_properties = d
        return signature_options

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
