from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.credential_context_item import CredentialContextItem
from ..models.credential_credential_subject import CredentialCredentialSubject
from ..models.credential_issuer import CredentialIssuer
from ..models.linked_data_proof import LinkedDataProof
from ..types import UNSET, Unset

T = TypeVar("T", bound="Credential")


@attr.s(auto_attribs=True)
class Credential:
    """ """

    context: List[CredentialContextItem]
    credential_subject: CredentialCredentialSubject
    issuance_date: str
    issuer: CredentialIssuer
    type: List[str]
    expiration_date: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    proof: Union[Unset, LinkedDataProof] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        context = []
        for context_item_data in self.context:
            context_item = context_item_data.to_dict()

            context.append(context_item)

        credential_subject = self.credential_subject.to_dict()

        issuance_date = self.issuance_date
        issuer = self.issuer.to_dict()

        type = self.type

        expiration_date = self.expiration_date
        id = self.id
        proof: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.proof, Unset):
            proof = self.proof.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "@context": context,
                "credentialSubject": credential_subject,
                "issuanceDate": issuance_date,
                "issuer": issuer,
                "type": type,
            }
        )
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
        if id is not UNSET:
            field_dict["id"] = id
        if proof is not UNSET:
            field_dict["proof"] = proof

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        context = []
        _context = d.pop("@context")
        for context_item_data in _context:
            context_item = CredentialContextItem.from_dict(context_item_data)

            context.append(context_item)

        credential_subject = CredentialCredentialSubject.from_dict(d.pop("credentialSubject"))

        issuance_date = d.pop("issuanceDate")

        issuer = CredentialIssuer.from_dict(d.pop("issuer"))

        type = cast(List[str], d.pop("type"))

        expiration_date = d.pop("expirationDate", UNSET)

        id = d.pop("id", UNSET)

        _proof = d.pop("proof", UNSET)
        proof: Union[Unset, LinkedDataProof]
        if isinstance(_proof, Unset):
            proof = UNSET
        else:
            proof = LinkedDataProof.from_dict(_proof)

        credential = cls(
            context=context,
            credential_subject=credential_subject,
            issuance_date=issuance_date,
            issuer=issuer,
            type=type,
            expiration_date=expiration_date,
            id=id,
            proof=proof,
        )

        credential.additional_properties = d
        return credential

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
