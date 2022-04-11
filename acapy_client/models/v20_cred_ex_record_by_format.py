from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.v20_cred_ex_record_by_format_cred_issue import V20CredExRecordByFormatCredIssue
from ..models.v20_cred_ex_record_by_format_cred_offer import V20CredExRecordByFormatCredOffer
from ..models.v20_cred_ex_record_by_format_cred_proposal import V20CredExRecordByFormatCredProposal
from ..models.v20_cred_ex_record_by_format_cred_request import V20CredExRecordByFormatCredRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20CredExRecordByFormat")


@attr.s(auto_attribs=True)
class V20CredExRecordByFormat:
    """
    Attributes:
        cred_issue (Union[Unset, V20CredExRecordByFormatCredIssue]):
        cred_offer (Union[Unset, V20CredExRecordByFormatCredOffer]):
        cred_proposal (Union[Unset, V20CredExRecordByFormatCredProposal]):
        cred_request (Union[Unset, V20CredExRecordByFormatCredRequest]):
    """

    cred_issue: Union[Unset, V20CredExRecordByFormatCredIssue] = UNSET
    cred_offer: Union[Unset, V20CredExRecordByFormatCredOffer] = UNSET
    cred_proposal: Union[Unset, V20CredExRecordByFormatCredProposal] = UNSET
    cred_request: Union[Unset, V20CredExRecordByFormatCredRequest] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cred_issue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cred_issue, Unset):
            cred_issue = self.cred_issue.to_dict()

        cred_offer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cred_offer, Unset):
            cred_offer = self.cred_offer.to_dict()

        cred_proposal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cred_proposal, Unset):
            cred_proposal = self.cred_proposal.to_dict()

        cred_request: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cred_request, Unset):
            cred_request = self.cred_request.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cred_issue is not UNSET:
            field_dict["cred_issue"] = cred_issue
        if cred_offer is not UNSET:
            field_dict["cred_offer"] = cred_offer
        if cred_proposal is not UNSET:
            field_dict["cred_proposal"] = cred_proposal
        if cred_request is not UNSET:
            field_dict["cred_request"] = cred_request

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _cred_issue = d.pop("cred_issue", UNSET)
        cred_issue: Union[Unset, V20CredExRecordByFormatCredIssue]
        if isinstance(_cred_issue, Unset):
            cred_issue = UNSET
        else:
            cred_issue = V20CredExRecordByFormatCredIssue.from_dict(_cred_issue)

        _cred_offer = d.pop("cred_offer", UNSET)
        cred_offer: Union[Unset, V20CredExRecordByFormatCredOffer]
        if isinstance(_cred_offer, Unset):
            cred_offer = UNSET
        else:
            cred_offer = V20CredExRecordByFormatCredOffer.from_dict(_cred_offer)

        _cred_proposal = d.pop("cred_proposal", UNSET)
        cred_proposal: Union[Unset, V20CredExRecordByFormatCredProposal]
        if isinstance(_cred_proposal, Unset):
            cred_proposal = UNSET
        else:
            cred_proposal = V20CredExRecordByFormatCredProposal.from_dict(_cred_proposal)

        _cred_request = d.pop("cred_request", UNSET)
        cred_request: Union[Unset, V20CredExRecordByFormatCredRequest]
        if isinstance(_cred_request, Unset):
            cred_request = UNSET
        else:
            cred_request = V20CredExRecordByFormatCredRequest.from_dict(_cred_request)

        v20_cred_ex_record_by_format = cls(
            cred_issue=cred_issue,
            cred_offer=cred_offer,
            cred_proposal=cred_proposal,
            cred_request=cred_request,
        )

        v20_cred_ex_record_by_format.additional_properties = d
        return v20_cred_ex_record_by_format

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
