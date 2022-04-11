from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="DIFPresSpecRevealDoc")


@attr.s(auto_attribs=True)
class DIFPresSpecRevealDoc:
    """reveal doc [JSON-LD frame] dict used to derive the credential when selective disclosure is required

    Example:
        {'@context': ['https://www.w3.org/2018/credentials/v1', 'https://w3id.org/security/bbs/v1'], '@explicit': True,
            '@requireAll': True, 'credentialSubject': {'@explicit': True, '@requireAll': True, 'Observation':
            [{'effectiveDateTime': {}, '@explicit': True, '@requireAll': True}]}, 'issuanceDate': {}, 'issuer': {}, 'type':
            ['VerifiableCredential', 'LabReport']}

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dif_pres_spec_reveal_doc = cls()

        dif_pres_spec_reveal_doc.additional_properties = d
        return dif_pres_spec_reveal_doc

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
