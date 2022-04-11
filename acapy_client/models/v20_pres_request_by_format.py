from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.dif_proof_request import DIFProofRequest
from ..models.indy_proof_request import IndyProofRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20PresRequestByFormat")


@attr.s(auto_attribs=True)
class V20PresRequestByFormat:
    """
    Attributes:
        dif (Union[Unset, DIFProofRequest]):
        indy (Union[Unset, IndyProofRequest]):
    """

    dif: Union[Unset, DIFProofRequest] = UNSET
    indy: Union[Unset, IndyProofRequest] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dif: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dif, Unset):
            dif = self.dif.to_dict()

        indy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.indy, Unset):
            indy = self.indy.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dif is not UNSET:
            field_dict["dif"] = dif
        if indy is not UNSET:
            field_dict["indy"] = indy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _dif = d.pop("dif", UNSET)
        dif: Union[Unset, DIFProofRequest]
        if isinstance(_dif, Unset):
            dif = UNSET
        else:
            dif = DIFProofRequest.from_dict(_dif)

        _indy = d.pop("indy", UNSET)
        indy: Union[Unset, IndyProofRequest]
        if isinstance(_indy, Unset):
            indy = UNSET
        else:
            indy = IndyProofRequest.from_dict(_indy)

        v20_pres_request_by_format = cls(
            dif=dif,
            indy=indy,
        )

        v20_pres_request_by_format.additional_properties = d
        return v20_pres_request_by_format

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
