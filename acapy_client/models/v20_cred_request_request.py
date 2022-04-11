from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="V20CredRequestRequest")


@attr.s(auto_attribs=True)
class V20CredRequestRequest:
    """
    Attributes:
        holder_did (Union[Unset, None, str]): Holder DID to substitute for the credentialSubject.id Example:
            did:key:ahsdkjahsdkjhaskjdhakjshdkajhsdkjahs.
    """

    holder_did: Union[Unset, None, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        holder_did = self.holder_did

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if holder_did is not UNSET:
            field_dict["holder_did"] = holder_did

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        holder_did = d.pop("holder_did", UNSET)

        v20_cred_request_request = cls(
            holder_did=holder_did,
        )

        v20_cred_request_request.additional_properties = d
        return v20_cred_request_request

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
