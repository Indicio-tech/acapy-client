from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.attach_decorator import AttachDecorator
from ..models.invitation_message_services_item import InvitationMessageServicesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="InvitationMessage")


@attr.s(auto_attribs=True)
class InvitationMessage:
    """
    Attributes:
        id (Union[Unset, str]): Message identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        type (Union[Unset, str]): Message type Example: https://didcomm.org/my-family/1.0/my-message-type.
        handshake_protocols (Union[Unset, List[str]]):
        label (Union[Unset, str]): Optional label Example: Bob.
        requestsattach (Union[Unset, List[AttachDecorator]]): Optional request attachment
        services (Union[Unset, List[InvitationMessageServicesItem]]):  Example: [{'did': 'WgWxqztrNooG92RXvxSTWv', 'id':
            'string', 'recipientKeys': ['did:key:z6MkpTHR8VNsBxYAAWHut2Geadd9jSwuBV8xRoAnwWsdvktH'], 'routingKeys':
            ['did:key:z6MkpTHR8VNsBxYAAWHut2Geadd9jSwuBV8xRoAnwWsdvktH'], 'serviceEndpoint': 'http://192.168.56.101:8020',
            'type': 'string'}, 'did:sov:WgWxqztrNooG92RXvxSTWv'].
    """

    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    handshake_protocols: Union[Unset, List[str]] = UNSET
    label: Union[Unset, str] = UNSET
    requestsattach: Union[Unset, List[AttachDecorator]] = UNSET
    services: Union[Unset, List[InvitationMessageServicesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type
        handshake_protocols: Union[Unset, List[str]] = UNSET
        if not isinstance(self.handshake_protocols, Unset):
            handshake_protocols = self.handshake_protocols

        label = self.label
        requestsattach: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.requestsattach, Unset):
            requestsattach = []
            for requestsattach_item_data in self.requestsattach:
                requestsattach_item = requestsattach_item_data.to_dict()

                requestsattach.append(requestsattach_item)

        services: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()

                services.append(services_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["@id"] = id
        if type is not UNSET:
            field_dict["@type"] = type
        if handshake_protocols is not UNSET:
            field_dict["handshake_protocols"] = handshake_protocols
        if label is not UNSET:
            field_dict["label"] = label
        if requestsattach is not UNSET:
            field_dict["requests~attach"] = requestsattach
        if services is not UNSET:
            field_dict["services"] = services

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("@id", UNSET)

        type = d.pop("@type", UNSET)

        handshake_protocols = cast(List[str], d.pop("handshake_protocols", UNSET))

        label = d.pop("label", UNSET)

        requestsattach = []
        _requestsattach = d.pop("requests~attach", UNSET)
        for requestsattach_item_data in _requestsattach or []:
            requestsattach_item = AttachDecorator.from_dict(requestsattach_item_data)

            requestsattach.append(requestsattach_item)

        services = []
        _services = d.pop("services", UNSET)
        for services_item_data in _services or []:
            services_item = InvitationMessageServicesItem.from_dict(services_item_data)

            services.append(services_item)

        invitation_message = cls(
            id=id,
            type=type,
            handshake_protocols=handshake_protocols,
            label=label,
            requestsattach=requestsattach,
            services=services,
        )

        invitation_message.additional_properties = d
        return invitation_message

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
