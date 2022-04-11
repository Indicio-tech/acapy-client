from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.signed_doc import SignedDoc
from ..types import UNSET, Unset

T = TypeVar("T", bound="VerifyRequest")


@attr.s(auto_attribs=True)
class VerifyRequest:
    """
    Attributes:
        doc (SignedDoc):
        verkey (Union[Unset, str]): Verkey to use for doc verification
    """

    doc: SignedDoc
    verkey: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        doc = self.doc.to_dict()

        verkey = self.verkey

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "doc": doc,
            }
        )
        if verkey is not UNSET:
            field_dict["verkey"] = verkey

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        doc = SignedDoc.from_dict(d.pop("doc"))

        verkey = d.pop("verkey", UNSET)

        verify_request = cls(
            doc=doc,
            verkey=verkey,
        )

        verify_request.additional_properties = d
        return verify_request

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
