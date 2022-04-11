from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.ld_proof_vc_detail import LDProofVCDetail
from ..models.v20_cred_filter_indy import V20CredFilterIndy
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20CredFilter")


@attr.s(auto_attribs=True)
class V20CredFilter:
    """
    Attributes:
        indy (Union[Unset, V20CredFilterIndy]):
        ld_proof (Union[Unset, LDProofVCDetail]):
    """

    indy: Union[Unset, V20CredFilterIndy] = UNSET
    ld_proof: Union[Unset, LDProofVCDetail] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        indy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.indy, Unset):
            indy = self.indy.to_dict()

        ld_proof: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ld_proof, Unset):
            ld_proof = self.ld_proof.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if indy is not UNSET:
            field_dict["indy"] = indy
        if ld_proof is not UNSET:
            field_dict["ld_proof"] = ld_proof

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _indy = d.pop("indy", UNSET)
        indy: Union[Unset, V20CredFilterIndy]
        if isinstance(_indy, Unset):
            indy = UNSET
        else:
            indy = V20CredFilterIndy.from_dict(_indy)

        _ld_proof = d.pop("ld_proof", UNSET)
        ld_proof: Union[Unset, LDProofVCDetail]
        if isinstance(_ld_proof, Unset):
            ld_proof = UNSET
        else:
            ld_proof = LDProofVCDetail.from_dict(_ld_proof)

        v20_cred_filter = cls(
            indy=indy,
            ld_proof=ld_proof,
        )

        v20_cred_filter.additional_properties = d
        return v20_cred_filter

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
