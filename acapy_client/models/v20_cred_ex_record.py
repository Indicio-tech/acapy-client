from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.v20_cred_ex_record_by_format import V20CredExRecordByFormat
from ..models.v20_cred_ex_record_initiator import V20CredExRecordInitiator
from ..models.v20_cred_ex_record_role import V20CredExRecordRole
from ..models.v20_cred_ex_record_state import V20CredExRecordState
from ..models.v20_cred_issue import V20CredIssue
from ..models.v20_cred_offer import V20CredOffer
from ..models.v20_cred_preview import V20CredPreview
from ..models.v20_cred_proposal import V20CredProposal
from ..models.v20_cred_request import V20CredRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20CredExRecord")


@attr.s(auto_attribs=True)
class V20CredExRecord:
    """
    Attributes:
        auto_issue (Union[Unset, bool]): Issuer choice to issue to request in this credential exchange
        auto_offer (Union[Unset, bool]): Holder choice to accept offer in this credential exchange
        auto_remove (Union[Unset, bool]): Issuer choice to remove this credential exchange record when complete
        by_format (Union[Unset, V20CredExRecordByFormat]):
        connection_id (Union[Unset, str]): Connection identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        created_at (Union[Unset, str]): Time of record creation Example: 2021-12-31 23:59:59+00:00.
        cred_ex_id (Union[Unset, str]): Credential exchange identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        cred_issue (Union[Unset, V20CredIssue]):
        cred_offer (Union[Unset, V20CredOffer]):
        cred_preview (Union[Unset, V20CredPreview]):
        cred_proposal (Union[Unset, V20CredProposal]):
        cred_request (Union[Unset, V20CredRequest]):
        error_msg (Union[Unset, str]): Error message Example: The front fell off.
        initiator (Union[Unset, V20CredExRecordInitiator]): Issue-credential exchange initiator: self or external
            Example: self.
        parent_thread_id (Union[Unset, str]): Parent thread identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        role (Union[Unset, V20CredExRecordRole]): Issue-credential exchange role: holder or issuer Example: issuer.
        state (Union[Unset, V20CredExRecordState]): Issue-credential exchange state Example: done.
        thread_id (Union[Unset, str]): Thread identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        trace (Union[Unset, bool]): Record trace information, based on agent configuration
        updated_at (Union[Unset, str]): Time of last record update Example: 2021-12-31 23:59:59+00:00.
    """

    auto_issue: Union[Unset, bool] = UNSET
    auto_offer: Union[Unset, bool] = UNSET
    auto_remove: Union[Unset, bool] = UNSET
    by_format: Union[Unset, V20CredExRecordByFormat] = UNSET
    connection_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    cred_ex_id: Union[Unset, str] = UNSET
    cred_issue: Union[Unset, V20CredIssue] = UNSET
    cred_offer: Union[Unset, V20CredOffer] = UNSET
    cred_preview: Union[Unset, V20CredPreview] = UNSET
    cred_proposal: Union[Unset, V20CredProposal] = UNSET
    cred_request: Union[Unset, V20CredRequest] = UNSET
    error_msg: Union[Unset, str] = UNSET
    initiator: Union[Unset, V20CredExRecordInitiator] = UNSET
    parent_thread_id: Union[Unset, str] = UNSET
    role: Union[Unset, V20CredExRecordRole] = UNSET
    state: Union[Unset, V20CredExRecordState] = UNSET
    thread_id: Union[Unset, str] = UNSET
    trace: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auto_issue = self.auto_issue
        auto_offer = self.auto_offer
        auto_remove = self.auto_remove
        by_format: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.by_format, Unset):
            by_format = self.by_format.to_dict()

        connection_id = self.connection_id
        created_at = self.created_at
        cred_ex_id = self.cred_ex_id
        cred_issue: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cred_issue, Unset):
            cred_issue = self.cred_issue.to_dict()

        cred_offer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cred_offer, Unset):
            cred_offer = self.cred_offer.to_dict()

        cred_preview: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cred_preview, Unset):
            cred_preview = self.cred_preview.to_dict()

        cred_proposal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cred_proposal, Unset):
            cred_proposal = self.cred_proposal.to_dict()

        cred_request: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cred_request, Unset):
            cred_request = self.cred_request.to_dict()

        error_msg = self.error_msg
        initiator: Union[Unset, str] = UNSET
        if not isinstance(self.initiator, Unset):
            initiator = self.initiator.value

        parent_thread_id = self.parent_thread_id
        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        thread_id = self.thread_id
        trace = self.trace
        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_issue is not UNSET:
            field_dict["auto_issue"] = auto_issue
        if auto_offer is not UNSET:
            field_dict["auto_offer"] = auto_offer
        if auto_remove is not UNSET:
            field_dict["auto_remove"] = auto_remove
        if by_format is not UNSET:
            field_dict["by_format"] = by_format
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if cred_ex_id is not UNSET:
            field_dict["cred_ex_id"] = cred_ex_id
        if cred_issue is not UNSET:
            field_dict["cred_issue"] = cred_issue
        if cred_offer is not UNSET:
            field_dict["cred_offer"] = cred_offer
        if cred_preview is not UNSET:
            field_dict["cred_preview"] = cred_preview
        if cred_proposal is not UNSET:
            field_dict["cred_proposal"] = cred_proposal
        if cred_request is not UNSET:
            field_dict["cred_request"] = cred_request
        if error_msg is not UNSET:
            field_dict["error_msg"] = error_msg
        if initiator is not UNSET:
            field_dict["initiator"] = initiator
        if parent_thread_id is not UNSET:
            field_dict["parent_thread_id"] = parent_thread_id
        if role is not UNSET:
            field_dict["role"] = role
        if state is not UNSET:
            field_dict["state"] = state
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if trace is not UNSET:
            field_dict["trace"] = trace
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auto_issue = d.pop("auto_issue", UNSET)

        auto_offer = d.pop("auto_offer", UNSET)

        auto_remove = d.pop("auto_remove", UNSET)

        _by_format = d.pop("by_format", UNSET)
        by_format: Union[Unset, V20CredExRecordByFormat]
        if isinstance(_by_format, Unset):
            by_format = UNSET
        else:
            by_format = V20CredExRecordByFormat.from_dict(_by_format)

        connection_id = d.pop("connection_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        cred_ex_id = d.pop("cred_ex_id", UNSET)

        _cred_issue = d.pop("cred_issue", UNSET)
        cred_issue: Union[Unset, V20CredIssue]
        if isinstance(_cred_issue, Unset):
            cred_issue = UNSET
        else:
            cred_issue = V20CredIssue.from_dict(_cred_issue)

        _cred_offer = d.pop("cred_offer", UNSET)
        cred_offer: Union[Unset, V20CredOffer]
        if isinstance(_cred_offer, Unset):
            cred_offer = UNSET
        else:
            cred_offer = V20CredOffer.from_dict(_cred_offer)

        _cred_preview = d.pop("cred_preview", UNSET)
        cred_preview: Union[Unset, V20CredPreview]
        if isinstance(_cred_preview, Unset):
            cred_preview = UNSET
        else:
            cred_preview = V20CredPreview.from_dict(_cred_preview)

        _cred_proposal = d.pop("cred_proposal", UNSET)
        cred_proposal: Union[Unset, V20CredProposal]
        if isinstance(_cred_proposal, Unset):
            cred_proposal = UNSET
        else:
            cred_proposal = V20CredProposal.from_dict(_cred_proposal)

        _cred_request = d.pop("cred_request", UNSET)
        cred_request: Union[Unset, V20CredRequest]
        if isinstance(_cred_request, Unset):
            cred_request = UNSET
        else:
            cred_request = V20CredRequest.from_dict(_cred_request)

        error_msg = d.pop("error_msg", UNSET)

        _initiator = d.pop("initiator", UNSET)
        initiator: Union[Unset, V20CredExRecordInitiator]
        if isinstance(_initiator, Unset):
            initiator = UNSET
        else:
            initiator = V20CredExRecordInitiator(_initiator)

        parent_thread_id = d.pop("parent_thread_id", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, V20CredExRecordRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = V20CredExRecordRole(_role)

        _state = d.pop("state", UNSET)
        state: Union[Unset, V20CredExRecordState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = V20CredExRecordState(_state)

        thread_id = d.pop("thread_id", UNSET)

        trace = d.pop("trace", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        v20_cred_ex_record = cls(
            auto_issue=auto_issue,
            auto_offer=auto_offer,
            auto_remove=auto_remove,
            by_format=by_format,
            connection_id=connection_id,
            created_at=created_at,
            cred_ex_id=cred_ex_id,
            cred_issue=cred_issue,
            cred_offer=cred_offer,
            cred_preview=cred_preview,
            cred_proposal=cred_proposal,
            cred_request=cred_request,
            error_msg=error_msg,
            initiator=initiator,
            parent_thread_id=parent_thread_id,
            role=role,
            state=state,
            thread_id=thread_id,
            trace=trace,
            updated_at=updated_at,
        )

        v20_cred_ex_record.additional_properties = d
        return v20_cred_ex_record

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
