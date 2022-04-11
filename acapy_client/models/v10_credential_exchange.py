from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.credential_offer import CredentialOffer
from ..models.credential_proposal import CredentialProposal
from ..models.indy_cred_abstract import IndyCredAbstract
from ..models.indy_cred_info import IndyCredInfo
from ..models.indy_cred_request import IndyCredRequest
from ..models.indy_credential import IndyCredential
from ..models.v10_credential_exchange_credential_request_metadata import V10CredentialExchangeCredentialRequestMetadata
from ..models.v10_credential_exchange_initiator import V10CredentialExchangeInitiator
from ..models.v10_credential_exchange_role import V10CredentialExchangeRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="V10CredentialExchange")


@attr.s(auto_attribs=True)
class V10CredentialExchange:
    """
    Attributes:
        auto_issue (Union[Unset, bool]): Issuer choice to issue to request in this credential exchange
        auto_offer (Union[Unset, bool]): Holder choice to accept offer in this credential exchange
        auto_remove (Union[Unset, bool]): Issuer choice to remove this credential exchange record when complete
        connection_id (Union[Unset, str]): Connection identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        created_at (Union[Unset, str]): Time of record creation Example: 2021-12-31 23:59:59+00:00.
        credential (Union[Unset, IndyCredInfo]):
        credential_definition_id (Union[Unset, str]): Credential definition identifier Example:
            WgWxqztrNooG92RXvxSTWv:3:CL:20:tag.
        credential_exchange_id (Union[Unset, str]): Credential exchange identifier Example:
            3fa85f64-5717-4562-b3fc-2c963f66afa6.
        credential_id (Union[Unset, str]): Credential identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        credential_offer (Union[Unset, IndyCredAbstract]):
        credential_offer_dict (Union[Unset, CredentialOffer]):
        credential_proposal_dict (Union[Unset, CredentialProposal]):
        credential_request (Union[Unset, IndyCredRequest]):
        credential_request_metadata (Union[Unset, V10CredentialExchangeCredentialRequestMetadata]): (Indy) credential
            request metadata
        error_msg (Union[Unset, str]): Error message Example: Credential definition identifier is not set in proposal.
        initiator (Union[Unset, V10CredentialExchangeInitiator]): Issue-credential exchange initiator: self or external
            Example: self.
        parent_thread_id (Union[Unset, str]): Parent thread identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        raw_credential (Union[Unset, IndyCredential]):
        revoc_reg_id (Union[Unset, str]): Revocation registry identifier
        revocation_id (Union[Unset, str]): Credential identifier within revocation registry
        role (Union[Unset, V10CredentialExchangeRole]): Issue-credential exchange role: holder or issuer Example:
            issuer.
        schema_id (Union[Unset, str]): Schema identifier Example: WgWxqztrNooG92RXvxSTWv:2:schema_name:1.0.
        state (Union[Unset, str]): Issue-credential exchange state Example: credential_acked.
        thread_id (Union[Unset, str]): Thread identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        trace (Union[Unset, bool]): Record trace information, based on agent configuration
        updated_at (Union[Unset, str]): Time of last record update Example: 2021-12-31 23:59:59+00:00.
    """

    auto_issue: Union[Unset, bool] = UNSET
    auto_offer: Union[Unset, bool] = UNSET
    auto_remove: Union[Unset, bool] = UNSET
    connection_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    credential: Union[Unset, IndyCredInfo] = UNSET
    credential_definition_id: Union[Unset, str] = UNSET
    credential_exchange_id: Union[Unset, str] = UNSET
    credential_id: Union[Unset, str] = UNSET
    credential_offer: Union[Unset, IndyCredAbstract] = UNSET
    credential_offer_dict: Union[Unset, CredentialOffer] = UNSET
    credential_proposal_dict: Union[Unset, CredentialProposal] = UNSET
    credential_request: Union[Unset, IndyCredRequest] = UNSET
    credential_request_metadata: Union[Unset, V10CredentialExchangeCredentialRequestMetadata] = UNSET
    error_msg: Union[Unset, str] = UNSET
    initiator: Union[Unset, V10CredentialExchangeInitiator] = UNSET
    parent_thread_id: Union[Unset, str] = UNSET
    raw_credential: Union[Unset, IndyCredential] = UNSET
    revoc_reg_id: Union[Unset, str] = UNSET
    revocation_id: Union[Unset, str] = UNSET
    role: Union[Unset, V10CredentialExchangeRole] = UNSET
    schema_id: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    thread_id: Union[Unset, str] = UNSET
    trace: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        auto_issue = self.auto_issue
        auto_offer = self.auto_offer
        auto_remove = self.auto_remove
        connection_id = self.connection_id
        created_at = self.created_at
        credential: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential, Unset):
            credential = self.credential.to_dict()

        credential_definition_id = self.credential_definition_id
        credential_exchange_id = self.credential_exchange_id
        credential_id = self.credential_id
        credential_offer: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_offer, Unset):
            credential_offer = self.credential_offer.to_dict()

        credential_offer_dict: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_offer_dict, Unset):
            credential_offer_dict = self.credential_offer_dict.to_dict()

        credential_proposal_dict: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_proposal_dict, Unset):
            credential_proposal_dict = self.credential_proposal_dict.to_dict()

        credential_request: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_request, Unset):
            credential_request = self.credential_request.to_dict()

        credential_request_metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_request_metadata, Unset):
            credential_request_metadata = self.credential_request_metadata.to_dict()

        error_msg = self.error_msg
        initiator: Union[Unset, str] = UNSET
        if not isinstance(self.initiator, Unset):
            initiator = self.initiator.value

        parent_thread_id = self.parent_thread_id
        raw_credential: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.raw_credential, Unset):
            raw_credential = self.raw_credential.to_dict()

        revoc_reg_id = self.revoc_reg_id
        revocation_id = self.revocation_id
        role: Union[Unset, str] = UNSET
        if not isinstance(self.role, Unset):
            role = self.role.value

        schema_id = self.schema_id
        state = self.state
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
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if credential is not UNSET:
            field_dict["credential"] = credential
        if credential_definition_id is not UNSET:
            field_dict["credential_definition_id"] = credential_definition_id
        if credential_exchange_id is not UNSET:
            field_dict["credential_exchange_id"] = credential_exchange_id
        if credential_id is not UNSET:
            field_dict["credential_id"] = credential_id
        if credential_offer is not UNSET:
            field_dict["credential_offer"] = credential_offer
        if credential_offer_dict is not UNSET:
            field_dict["credential_offer_dict"] = credential_offer_dict
        if credential_proposal_dict is not UNSET:
            field_dict["credential_proposal_dict"] = credential_proposal_dict
        if credential_request is not UNSET:
            field_dict["credential_request"] = credential_request
        if credential_request_metadata is not UNSET:
            field_dict["credential_request_metadata"] = credential_request_metadata
        if error_msg is not UNSET:
            field_dict["error_msg"] = error_msg
        if initiator is not UNSET:
            field_dict["initiator"] = initiator
        if parent_thread_id is not UNSET:
            field_dict["parent_thread_id"] = parent_thread_id
        if raw_credential is not UNSET:
            field_dict["raw_credential"] = raw_credential
        if revoc_reg_id is not UNSET:
            field_dict["revoc_reg_id"] = revoc_reg_id
        if revocation_id is not UNSET:
            field_dict["revocation_id"] = revocation_id
        if role is not UNSET:
            field_dict["role"] = role
        if schema_id is not UNSET:
            field_dict["schema_id"] = schema_id
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

        connection_id = d.pop("connection_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        _credential = d.pop("credential", UNSET)
        credential: Union[Unset, IndyCredInfo]
        if isinstance(_credential, Unset):
            credential = UNSET
        else:
            credential = IndyCredInfo.from_dict(_credential)

        credential_definition_id = d.pop("credential_definition_id", UNSET)

        credential_exchange_id = d.pop("credential_exchange_id", UNSET)

        credential_id = d.pop("credential_id", UNSET)

        _credential_offer = d.pop("credential_offer", UNSET)
        credential_offer: Union[Unset, IndyCredAbstract]
        if isinstance(_credential_offer, Unset):
            credential_offer = UNSET
        else:
            credential_offer = IndyCredAbstract.from_dict(_credential_offer)

        _credential_offer_dict = d.pop("credential_offer_dict", UNSET)
        credential_offer_dict: Union[Unset, CredentialOffer]
        if isinstance(_credential_offer_dict, Unset):
            credential_offer_dict = UNSET
        else:
            credential_offer_dict = CredentialOffer.from_dict(_credential_offer_dict)

        _credential_proposal_dict = d.pop("credential_proposal_dict", UNSET)
        credential_proposal_dict: Union[Unset, CredentialProposal]
        if isinstance(_credential_proposal_dict, Unset):
            credential_proposal_dict = UNSET
        else:
            credential_proposal_dict = CredentialProposal.from_dict(_credential_proposal_dict)

        _credential_request = d.pop("credential_request", UNSET)
        credential_request: Union[Unset, IndyCredRequest]
        if isinstance(_credential_request, Unset):
            credential_request = UNSET
        else:
            credential_request = IndyCredRequest.from_dict(_credential_request)

        _credential_request_metadata = d.pop("credential_request_metadata", UNSET)
        credential_request_metadata: Union[Unset, V10CredentialExchangeCredentialRequestMetadata]
        if isinstance(_credential_request_metadata, Unset):
            credential_request_metadata = UNSET
        else:
            credential_request_metadata = V10CredentialExchangeCredentialRequestMetadata.from_dict(
                _credential_request_metadata
            )

        error_msg = d.pop("error_msg", UNSET)

        _initiator = d.pop("initiator", UNSET)
        initiator: Union[Unset, V10CredentialExchangeInitiator]
        if isinstance(_initiator, Unset):
            initiator = UNSET
        else:
            initiator = V10CredentialExchangeInitiator(_initiator)

        parent_thread_id = d.pop("parent_thread_id", UNSET)

        _raw_credential = d.pop("raw_credential", UNSET)
        raw_credential: Union[Unset, IndyCredential]
        if isinstance(_raw_credential, Unset):
            raw_credential = UNSET
        else:
            raw_credential = IndyCredential.from_dict(_raw_credential)

        revoc_reg_id = d.pop("revoc_reg_id", UNSET)

        revocation_id = d.pop("revocation_id", UNSET)

        _role = d.pop("role", UNSET)
        role: Union[Unset, V10CredentialExchangeRole]
        if isinstance(_role, Unset):
            role = UNSET
        else:
            role = V10CredentialExchangeRole(_role)

        schema_id = d.pop("schema_id", UNSET)

        state = d.pop("state", UNSET)

        thread_id = d.pop("thread_id", UNSET)

        trace = d.pop("trace", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        v10_credential_exchange = cls(
            auto_issue=auto_issue,
            auto_offer=auto_offer,
            auto_remove=auto_remove,
            connection_id=connection_id,
            created_at=created_at,
            credential=credential,
            credential_definition_id=credential_definition_id,
            credential_exchange_id=credential_exchange_id,
            credential_id=credential_id,
            credential_offer=credential_offer,
            credential_offer_dict=credential_offer_dict,
            credential_proposal_dict=credential_proposal_dict,
            credential_request=credential_request,
            credential_request_metadata=credential_request_metadata,
            error_msg=error_msg,
            initiator=initiator,
            parent_thread_id=parent_thread_id,
            raw_credential=raw_credential,
            revoc_reg_id=revoc_reg_id,
            revocation_id=revocation_id,
            role=role,
            schema_id=schema_id,
            state=state,
            thread_id=thread_id,
            trace=trace,
            updated_at=updated_at,
        )

        v10_credential_exchange.additional_properties = d
        return v10_credential_exchange

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
