from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.sign_response_signed_doc import SignResponseSignedDoc
from ..types import UNSET, Unset

T = TypeVar("T", bound="SignResponse")


@attr.s(auto_attribs=True)
class SignResponse:
    """
    Attributes:
        error (Union[Unset, str]): Error text
        signed_doc (Union[Unset, SignResponseSignedDoc]): Signed document
    """

    error: Union[Unset, str] = UNSET
    signed_doc: Union[Unset, SignResponseSignedDoc] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        error = self.error
        signed_doc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.signed_doc, Unset):
            signed_doc = self.signed_doc.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if error is not UNSET:
            field_dict["error"] = error
        if signed_doc is not UNSET:
            field_dict["signed_doc"] = signed_doc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        error = d.pop("error", UNSET)

        _signed_doc = d.pop("signed_doc", UNSET)
        signed_doc: Union[Unset, SignResponseSignedDoc]
        if isinstance(_signed_doc, Unset):
            signed_doc = UNSET
        else:
            signed_doc = SignResponseSignedDoc.from_dict(_signed_doc)

        sign_response = cls(
            error=error,
            signed_doc=signed_doc,
        )

        sign_response.additional_properties = d
        return sign_response

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
