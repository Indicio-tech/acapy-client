from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.indy_key_correctness_proof import IndyKeyCorrectnessProof

T = TypeVar("T", bound="IndyCredAbstract")


@attr.s(auto_attribs=True)
class IndyCredAbstract:
    """
    Attributes:
        cred_def_id (str): Credential definition identifier Example: WgWxqztrNooG92RXvxSTWv:3:CL:20:tag.
        key_correctness_proof (IndyKeyCorrectnessProof):
        nonce (str): Nonce in credential abstract Example: 0.
        schema_id (str): Schema identifier Example: WgWxqztrNooG92RXvxSTWv:2:schema_name:1.0.
    """

    cred_def_id: str
    key_correctness_proof: IndyKeyCorrectnessProof
    nonce: str
    schema_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cred_def_id = self.cred_def_id
        key_correctness_proof = self.key_correctness_proof.to_dict()

        nonce = self.nonce
        schema_id = self.schema_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cred_def_id": cred_def_id,
                "key_correctness_proof": key_correctness_proof,
                "nonce": nonce,
                "schema_id": schema_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cred_def_id = d.pop("cred_def_id")

        key_correctness_proof = IndyKeyCorrectnessProof.from_dict(d.pop("key_correctness_proof"))

        nonce = d.pop("nonce")

        schema_id = d.pop("schema_id")

        indy_cred_abstract = cls(
            cred_def_id=cred_def_id,
            key_correctness_proof=key_correctness_proof,
            nonce=nonce,
            schema_id=schema_id,
        )

        indy_cred_abstract.additional_properties = d
        return indy_cred_abstract

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
