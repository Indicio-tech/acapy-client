from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.create_invitation_request_metadata import CreateInvitationRequestMetadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateInvitationRequest")


@attr.s(auto_attribs=True)
class CreateInvitationRequest:
    """
    Attributes:
        mediation_id (Union[Unset, str]): Identifier for active mediation record to be used Example:
            3fa85f64-5717-4562-b3fc-2c963f66afa6.
        metadata (Union[Unset, CreateInvitationRequestMetadata]): Optional metadata to attach to the connection created
            with the invitation
        my_label (Union[Unset, str]): Optional label for connection invitation Example: Bob.
        recipient_keys (Union[Unset, List[str]]): List of recipient keys
        routing_keys (Union[Unset, List[str]]): List of routing keys
        service_endpoint (Union[Unset, str]): Connection endpoint Example: http://192.168.56.102:8020.
    """

    mediation_id: Union[Unset, str] = UNSET
    metadata: Union[Unset, CreateInvitationRequestMetadata] = UNSET
    my_label: Union[Unset, str] = UNSET
    recipient_keys: Union[Unset, List[str]] = UNSET
    routing_keys: Union[Unset, List[str]] = UNSET
    service_endpoint: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mediation_id = self.mediation_id
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        my_label = self.my_label
        recipient_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.recipient_keys, Unset):
            recipient_keys = self.recipient_keys

        routing_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.routing_keys, Unset):
            routing_keys = self.routing_keys

        service_endpoint = self.service_endpoint

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mediation_id is not UNSET:
            field_dict["mediation_id"] = mediation_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if my_label is not UNSET:
            field_dict["my_label"] = my_label
        if recipient_keys is not UNSET:
            field_dict["recipient_keys"] = recipient_keys
        if routing_keys is not UNSET:
            field_dict["routing_keys"] = routing_keys
        if service_endpoint is not UNSET:
            field_dict["service_endpoint"] = service_endpoint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mediation_id = d.pop("mediation_id", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, CreateInvitationRequestMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateInvitationRequestMetadata.from_dict(_metadata)

        my_label = d.pop("my_label", UNSET)

        recipient_keys = cast(List[str], d.pop("recipient_keys", UNSET))

        routing_keys = cast(List[str], d.pop("routing_keys", UNSET))

        service_endpoint = d.pop("service_endpoint", UNSET)

        create_invitation_request = cls(
            mediation_id=mediation_id,
            metadata=metadata,
            my_label=my_label,
            recipient_keys=recipient_keys,
            routing_keys=routing_keys,
            service_endpoint=service_endpoint,
        )

        create_invitation_request.additional_properties = d
        return create_invitation_request

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
