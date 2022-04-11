from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.v20_pres_ex_record_by_format_pres import V20PresExRecordByFormatPres
from ..models.v20_pres_ex_record_by_format_pres_proposal import V20PresExRecordByFormatPresProposal
from ..models.v20_pres_ex_record_by_format_pres_request import V20PresExRecordByFormatPresRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20PresExRecordByFormat")


@attr.s(auto_attribs=True)
class V20PresExRecordByFormat:
    """
    Attributes:
        pres (Union[Unset, V20PresExRecordByFormatPres]):
        pres_proposal (Union[Unset, V20PresExRecordByFormatPresProposal]):
        pres_request (Union[Unset, V20PresExRecordByFormatPresRequest]):
    """

    pres: Union[Unset, V20PresExRecordByFormatPres] = UNSET
    pres_proposal: Union[Unset, V20PresExRecordByFormatPresProposal] = UNSET
    pres_request: Union[Unset, V20PresExRecordByFormatPresRequest] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pres: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pres, Unset):
            pres = self.pres.to_dict()

        pres_proposal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pres_proposal, Unset):
            pres_proposal = self.pres_proposal.to_dict()

        pres_request: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pres_request, Unset):
            pres_request = self.pres_request.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pres is not UNSET:
            field_dict["pres"] = pres
        if pres_proposal is not UNSET:
            field_dict["pres_proposal"] = pres_proposal
        if pres_request is not UNSET:
            field_dict["pres_request"] = pres_request

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _pres = d.pop("pres", UNSET)
        pres: Union[Unset, V20PresExRecordByFormatPres]
        if isinstance(_pres, Unset):
            pres = UNSET
        else:
            pres = V20PresExRecordByFormatPres.from_dict(_pres)

        _pres_proposal = d.pop("pres_proposal", UNSET)
        pres_proposal: Union[Unset, V20PresExRecordByFormatPresProposal]
        if isinstance(_pres_proposal, Unset):
            pres_proposal = UNSET
        else:
            pres_proposal = V20PresExRecordByFormatPresProposal.from_dict(_pres_proposal)

        _pres_request = d.pop("pres_request", UNSET)
        pres_request: Union[Unset, V20PresExRecordByFormatPresRequest]
        if isinstance(_pres_request, Unset):
            pres_request = UNSET
        else:
            pres_request = V20PresExRecordByFormatPresRequest.from_dict(_pres_request)

        v20_pres_ex_record_by_format = cls(
            pres=pres,
            pres_proposal=pres_proposal,
            pres_request=pres_request,
        )

        v20_pres_ex_record_by_format.additional_properties = d
        return v20_pres_ex_record_by_format

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
