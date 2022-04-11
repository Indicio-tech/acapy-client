from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.conn_record_accept import ConnRecordAccept
from ..models.conn_record_connection_protocol import ConnRecordConnectionProtocol
from ..models.conn_record_invitation_mode import ConnRecordInvitationMode
from ..models.conn_record_routing_state import ConnRecordRoutingState
from ..models.conn_record_their_role import ConnRecordTheirRole
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnRecord")


@attr.s(auto_attribs=True)
class ConnRecord:
    """
    Attributes:
        accept (Union[Unset, ConnRecordAccept]): Connection acceptance: manual or auto Example: auto.
        alias (Union[Unset, str]): Optional alias to apply to connection for later use Example: Bob, providing quotes.
        connection_id (Union[Unset, str]): Connection identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        connection_protocol (Union[Unset, ConnRecordConnectionProtocol]): Connection protocol used Example:
            connections/1.0.
        created_at (Union[Unset, str]): Time of record creation Example: 2021-12-31 23:59:59+00:00.
        error_msg (Union[Unset, str]): Error message Example: No DIDDoc provided; cannot connect to public DID.
        inbound_connection_id (Union[Unset, str]): Inbound routing connection id to use Example:
            3fa85f64-5717-4562-b3fc-2c963f66afa6.
        invitation_key (Union[Unset, str]): Public key for connection Example:
            H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV.
        invitation_mode (Union[Unset, ConnRecordInvitationMode]): Invitation mode Example: once.
        invitation_msg_id (Union[Unset, str]): ID of out-of-band invitation message Example:
            3fa85f64-5717-4562-b3fc-2c963f66afa6.
        my_did (Union[Unset, str]): Our DID for connection Example: WgWxqztrNooG92RXvxSTWv.
        request_id (Union[Unset, str]): Connection request identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        rfc23_state (Union[Unset, str]): State per RFC 23 Example: invitation-sent.
        routing_state (Union[Unset, ConnRecordRoutingState]): Routing state of connection Example: active.
        state (Union[Unset, str]): Current record state Example: active.
        their_did (Union[Unset, str]): Their DID for connection Example: WgWxqztrNooG92RXvxSTWv.
        their_label (Union[Unset, str]): Their label for connection Example: Bob.
        their_public_did (Union[Unset, str]): Other agent's public DID for connection Example: 2cpBmR3FqGKWi5EyUbpRY8.
        their_role (Union[Unset, ConnRecordTheirRole]): Their role in the connection protocol Example: requester.
        updated_at (Union[Unset, str]): Time of last record update Example: 2021-12-31 23:59:59+00:00.
    """

    accept: Union[Unset, ConnRecordAccept] = UNSET
    alias: Union[Unset, str] = UNSET
    connection_id: Union[Unset, str] = UNSET
    connection_protocol: Union[Unset, ConnRecordConnectionProtocol] = UNSET
    created_at: Union[Unset, str] = UNSET
    error_msg: Union[Unset, str] = UNSET
    inbound_connection_id: Union[Unset, str] = UNSET
    invitation_key: Union[Unset, str] = UNSET
    invitation_mode: Union[Unset, ConnRecordInvitationMode] = UNSET
    invitation_msg_id: Union[Unset, str] = UNSET
    my_did: Union[Unset, str] = UNSET
    request_id: Union[Unset, str] = UNSET
    rfc23_state: Union[Unset, str] = UNSET
    routing_state: Union[Unset, ConnRecordRoutingState] = UNSET
    state: Union[Unset, str] = UNSET
    their_did: Union[Unset, str] = UNSET
    their_label: Union[Unset, str] = UNSET
    their_public_did: Union[Unset, str] = UNSET
    their_role: Union[Unset, ConnRecordTheirRole] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accept: Union[Unset, str] = UNSET
        if not isinstance(self.accept, Unset):
            accept = self.accept.value

        alias = self.alias
        connection_id = self.connection_id
        connection_protocol: Union[Unset, str] = UNSET
        if not isinstance(self.connection_protocol, Unset):
            connection_protocol = self.connection_protocol.value

        created_at = self.created_at
        error_msg = self.error_msg
        inbound_connection_id = self.inbound_connection_id
        invitation_key = self.invitation_key
        invitation_mode: Union[Unset, str] = UNSET
        if not isinstance(self.invitation_mode, Unset):
            invitation_mode = self.invitation_mode.value

        invitation_msg_id = self.invitation_msg_id
        my_did = self.my_did
        request_id = self.request_id
        rfc23_state = self.rfc23_state
        routing_state: Union[Unset, str] = UNSET
        if not isinstance(self.routing_state, Unset):
            routing_state = self.routing_state.value

        state = self.state
        their_did = self.their_did
        their_label = self.their_label
        their_public_did = self.their_public_did
        their_role: Union[Unset, str] = UNSET
        if not isinstance(self.their_role, Unset):
            their_role = self.their_role.value

        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accept is not UNSET:
            field_dict["accept"] = accept
        if alias is not UNSET:
            field_dict["alias"] = alias
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if connection_protocol is not UNSET:
            field_dict["connection_protocol"] = connection_protocol
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if error_msg is not UNSET:
            field_dict["error_msg"] = error_msg
        if inbound_connection_id is not UNSET:
            field_dict["inbound_connection_id"] = inbound_connection_id
        if invitation_key is not UNSET:
            field_dict["invitation_key"] = invitation_key
        if invitation_mode is not UNSET:
            field_dict["invitation_mode"] = invitation_mode
        if invitation_msg_id is not UNSET:
            field_dict["invitation_msg_id"] = invitation_msg_id
        if my_did is not UNSET:
            field_dict["my_did"] = my_did
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if rfc23_state is not UNSET:
            field_dict["rfc23_state"] = rfc23_state
        if routing_state is not UNSET:
            field_dict["routing_state"] = routing_state
        if state is not UNSET:
            field_dict["state"] = state
        if their_did is not UNSET:
            field_dict["their_did"] = their_did
        if their_label is not UNSET:
            field_dict["their_label"] = their_label
        if their_public_did is not UNSET:
            field_dict["their_public_did"] = their_public_did
        if their_role is not UNSET:
            field_dict["their_role"] = their_role
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _accept = d.pop("accept", UNSET)
        accept: Union[Unset, ConnRecordAccept]
        if isinstance(_accept, Unset):
            accept = UNSET
        else:
            accept = ConnRecordAccept(_accept)

        alias = d.pop("alias", UNSET)

        connection_id = d.pop("connection_id", UNSET)

        _connection_protocol = d.pop("connection_protocol", UNSET)
        connection_protocol: Union[Unset, ConnRecordConnectionProtocol]
        if isinstance(_connection_protocol, Unset):
            connection_protocol = UNSET
        else:
            connection_protocol = ConnRecordConnectionProtocol(_connection_protocol)

        created_at = d.pop("created_at", UNSET)

        error_msg = d.pop("error_msg", UNSET)

        inbound_connection_id = d.pop("inbound_connection_id", UNSET)

        invitation_key = d.pop("invitation_key", UNSET)

        _invitation_mode = d.pop("invitation_mode", UNSET)
        invitation_mode: Union[Unset, ConnRecordInvitationMode]
        if isinstance(_invitation_mode, Unset):
            invitation_mode = UNSET
        else:
            invitation_mode = ConnRecordInvitationMode(_invitation_mode)

        invitation_msg_id = d.pop("invitation_msg_id", UNSET)

        my_did = d.pop("my_did", UNSET)

        request_id = d.pop("request_id", UNSET)

        rfc23_state = d.pop("rfc23_state", UNSET)

        _routing_state = d.pop("routing_state", UNSET)
        routing_state: Union[Unset, ConnRecordRoutingState]
        if isinstance(_routing_state, Unset):
            routing_state = UNSET
        else:
            routing_state = ConnRecordRoutingState(_routing_state)

        state = d.pop("state", UNSET)

        their_did = d.pop("their_did", UNSET)

        their_label = d.pop("their_label", UNSET)

        their_public_did = d.pop("their_public_did", UNSET)

        _their_role = d.pop("their_role", UNSET)
        their_role: Union[Unset, ConnRecordTheirRole]
        if isinstance(_their_role, Unset):
            their_role = UNSET
        else:
            their_role = ConnRecordTheirRole(_their_role)

        updated_at = d.pop("updated_at", UNSET)

        conn_record = cls(
            accept=accept,
            alias=alias,
            connection_id=connection_id,
            connection_protocol=connection_protocol,
            created_at=created_at,
            error_msg=error_msg,
            inbound_connection_id=inbound_connection_id,
            invitation_key=invitation_key,
            invitation_mode=invitation_mode,
            invitation_msg_id=invitation_msg_id,
            my_did=my_did,
            request_id=request_id,
            rfc23_state=rfc23_state,
            routing_state=routing_state,
            state=state,
            their_did=their_did,
            their_label=their_label,
            their_public_did=their_public_did,
            their_role=their_role,
            updated_at=updated_at,
        )

        conn_record.additional_properties = d
        return conn_record

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
