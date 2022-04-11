from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.doc_credential import DocCredential
from ..models.signature_options import SignatureOptions

T = TypeVar("T", bound="Doc")


@attr.s(auto_attribs=True)
class Doc:
    """
    Attributes:
        credential (DocCredential): Credential to sign
        options (SignatureOptions):
    """

    credential: DocCredential
    options: SignatureOptions
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credential = self.credential.to_dict()

        options = self.options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credential": credential,
                "options": options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credential = DocCredential.from_dict(d.pop("credential"))

        options = SignatureOptions.from_dict(d.pop("options"))

        doc = cls(
            credential=credential,
            options=options,
        )

        doc.additional_properties = d
        return doc

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
