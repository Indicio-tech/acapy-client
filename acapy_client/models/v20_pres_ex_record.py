from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.v20_pres import V20Pres
from ..models.v20_pres_ex_record_by_format import V20PresExRecordByFormat
from ..models.v20_pres_ex_record_initiator import V20PresExRecordInitiator
from ..models.v20_pres_ex_record_role import V20PresExRecordRole
from ..models.v20_pres_ex_record_state import V20PresExRecordState
from ..models.v20_pres_ex_record_verified import V20PresExRecordVerified
from ..models.v20_pres_proposal import V20PresProposal
from ..models.v20_pres_request import V20PresRequest
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20PresExRecord")


@attr.s(auto_attribs=True)
class V20PresExRecord:
    """
    Attributes:
        auto_present (Union[Unset, bool]): Prover choice to auto-present proof as verifier requests
        auto_verify (Union[Unset, bool]): Verifier choice to auto-verify proof presentation
        by_format (Union[Unset, V20PresExRecordByFormat]):
        connection_id (Union[Unset, str]): Connection identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        created_at (Union[Unset, str]): Time of record creation Example: 2021-12-31 23:59:59+00:00.
        error_msg (Union[Unset, str]): Error message Example: Invalid structure.
        initiator (Union[Unset, V20PresExRecordInitiator]): Present-proof exchange initiator: self or external Example:
            self.
        pres (Union[Unset, V20Pres]):
        pres_ex_id (Union[Unset, str]): Presentation exchange identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        pres_proposal (Union[Unset, V20PresProposal]):
        pres_request (Union[Unset, V20PresRequest]):
        role (Union[Unset, V20PresExRecordRole]): Present-proof exchange role: prover or verifier Example: prover.
        state (Union[Unset, V20PresExRecordState]): Present-proof exchange state
        thread_id (Union[Unset, str]): Thread identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        trace (Union[Unset, bool]): Record trace information, based on agent configuration
        updated_at (Union[Unset, str]): Time of last record update Example: 2021-12-31 23:59:59+00:00.
        verified (Union[Unset, V20PresExRecordVerified]): Whether presentation is verified: 'true' or 'false' Example:
            true.
    """

    auto_present: Union[Unset, bool] = UNSET
    auto_verify: Union[Unset, bool] = UNSET
    by_format: Union[Unset, V20PresExRecordByFormat] = UNSET
    connection_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    error_msg: Union[Unset, str] = UNSET
    initiator: Union[Unset, V20PresExRecordInitiator] = UNSET
    pres: Union[Unset, V20Pres] = UNSET
    pres_ex_id: Union[Unset, str] = UNSET
    pres_proposal: Union[Unset, V20PresProposal] = UNSET
    pres_request: Union[Unset, V20PresRequest] = UNSET
    role: Union[Unset, V20PresExRecordRole] = UNSET
    state: Union[Unset, V20PresExRecordState] = UNSET
    thread_id: Union[Unset, str] = UNSET
    trace: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    verified: Union[Unset, V20PresExRecordVerified] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auto_present = self.auto_present
        auto_verify = self.auto_verify
        by_format: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.by_format, Unset):
            by_format = self.by_format.to_dict()

        connection_id = self.connection_id
        created_at = self.created_at
        error_msg = self.error_msg
        initiator: Union[Unset, str] = UNSET
        if not isinstance(self.initiator, Unset):
            initiator = self.initiator.value

        pres: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pres, Unset):
            pres = self.pres.to_dict()

        pres_ex_id = self.pres_ex_id
        pres_proposal: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pres_proposal, Unset):
            pres_proposal = self.pres_proposal.to_dict()

        pres_request: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pres_request, Unset):
            pres_request = self.pres_request.to_dict()

        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        state: Union[Unset, str] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        thread_id = self.thread_id
        trace = self.trace
        updated_at = self.updated_at
        verified: Union[Unset, str] = UNSET
        if not isinstance(self.verified, Unset):
            verified = self.verified.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_present is not UNSET:
            field_dict["auto_present"] = auto_present
        if auto_verify is not UNSET:
            field_dict["auto_verify"] = auto_verify
        if by_format is not UNSET:
            field_dict["by_format"] = by_format
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if error_msg is not UNSET:
            field_dict["error_msg"] = error_msg
        if initiator is not UNSET:
            field_dict["initiator"] = initiator
        if pres is not UNSET:
            field_dict["pres"] = pres
        if pres_ex_id is not UNSET:
            field_dict["pres_ex_id"] = pres_ex_id
        if pres_proposal is not UNSET:
            field_dict["pres_proposal"] = pres_proposal
        if pres_request is not UNSET:
            field_dict["pres_request"] = pres_request
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
        if verified is not UNSET:
            field_dict["verified"] = verified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        auto_present = d.pop("auto_present", UNSET)

        auto_verify = d.pop("auto_verify", UNSET)

        _by_format = d.pop("by_format", UNSET)
        by_format: Union[Unset, V20PresExRecordByFormat]
        if isinstance(_by_format, Unset):
            by_format = UNSET
        else:
            by_format = V20PresExRecordByFormat.from_dict(_by_format)

        connection_id = d.pop("connection_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        error_msg = d.pop("error_msg", UNSET)

        _initiator = d.pop("initiator", UNSET)
        initiator: Union[Unset, V20PresExRecordInitiator]
        if isinstance(_initiator, Unset):
            initiator = UNSET
        else:
            initiator = V20PresExRecordInitiator(_initiator)

        _pres = d.pop("pres", UNSET)
        pres: Union[Unset, V20Pres]
        if isinstance(_pres, Unset):
            pres = UNSET
        else:
            pres = V20Pres.from_dict(_pres)

        pres_ex_id = d.pop("pres_ex_id", UNSET)

        _pres_proposal = d.pop("pres_proposal", UNSET)
        pres_proposal: Union[Unset, V20PresProposal]
        if isinstance(_pres_proposal, Unset):
            pres_proposal = UNSET
        else:
            pres_proposal = V20PresProposal.from_dict(_pres_proposal)

        _pres_request = d.pop("pres_request", UNSET)
        pres_request: Union[Unset, V20PresRequest]
        if isinstance(_pres_request, Unset):
            pres_request = UNSET
        else:
            pres_request = V20PresRequest.from_dict(_pres_request)

        _role = d.pop("role", UNSET)
        role: Union[Unset, V20PresExRecordRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = V20PresExRecordRole(_role)

        _state = d.pop("state", UNSET)
        state: Union[Unset, V20PresExRecordState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = V20PresExRecordState(_state)

        thread_id = d.pop("thread_id", UNSET)

        trace = d.pop("trace", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        _verified = d.pop("verified", UNSET)
        verified: Union[Unset, V20PresExRecordVerified]
        if isinstance(_verified, Unset):
            verified = UNSET
        else:
            verified = V20PresExRecordVerified(_verified)

        v20_pres_ex_record = cls(
            auto_present=auto_present,
            auto_verify=auto_verify,
            by_format=by_format,
            connection_id=connection_id,
            created_at=created_at,
            error_msg=error_msg,
            initiator=initiator,
            pres=pres,
            pres_ex_id=pres_ex_id,
            pres_proposal=pres_proposal,
            pres_request=pres_request,
            role=role,
            state=state,
            thread_id=thread_id,
            trace=trace,
            updated_at=updated_at,
            verified=verified,
        )

        v20_pres_ex_record.additional_properties = d
        return v20_pres_ex_record

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
