from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyProofReqPredSpecNonRevoked")


@attr.s(auto_attribs=True)
class IndyProofReqPredSpecNonRevoked:
    """
    Attributes:
        from_ (Union[Unset, int]): Earliest time of interest in non-revocation interval Example: 1640995199.
        to (Union[Unset, int]): Latest time of interest in non-revocation interval Example: 1640995199.
    """

    from_: Union[Unset, int] = UNSET
    to: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ = self.from_
        to = self.to

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        indy_proof_req_pred_spec_non_revoked = cls(
            from_=from_,
            to=to,
        )

        indy_proof_req_pred_spec_non_revoked.additional_properties = d
        return indy_proof_req_pred_spec_non_revoked

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
