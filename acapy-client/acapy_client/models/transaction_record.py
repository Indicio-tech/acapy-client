from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.transaction_record_formats_item import TransactionRecordFormatsItem
from ..models.transaction_record_messages_attach_item import TransactionRecordMessagesAttachItem
from ..models.transaction_record_signature_request_item import TransactionRecordSignatureRequestItem
from ..models.transaction_record_signature_response_item import TransactionRecordSignatureResponseItem
from ..models.transaction_record_timing import TransactionRecordTiming
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionRecord")


@attr.s(auto_attribs=True)
class TransactionRecord:
    """ """

    type: Union[Unset, str] = UNSET
    connection_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    endorser_write_txn: Union[Unset, bool] = UNSET
    formats: Union[Unset, List[TransactionRecordFormatsItem]] = UNSET
    messages_attach: Union[Unset, List[TransactionRecordMessagesAttachItem]] = UNSET
    signature_request: Union[Unset, List[TransactionRecordSignatureRequestItem]] = UNSET
    signature_response: Union[Unset, List[TransactionRecordSignatureResponseItem]] = UNSET
    state: Union[Unset, str] = UNSET
    thread_id: Union[Unset, str] = UNSET
    timing: Union[Unset, TransactionRecordTiming] = UNSET
    trace: Union[Unset, bool] = UNSET
    transaction_id: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        connection_id = self.connection_id
        created_at = self.created_at
        endorser_write_txn = self.endorser_write_txn
        formats: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.formats, Unset):
            formats = []
            for formats_item_data in self.formats:
                formats_item = formats_item_data.to_dict()

                formats.append(formats_item)

        messages_attach: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.messages_attach, Unset):
            messages_attach = []
            for messages_attach_item_data in self.messages_attach:
                messages_attach_item = messages_attach_item_data.to_dict()

                messages_attach.append(messages_attach_item)

        signature_request: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.signature_request, Unset):
            signature_request = []
            for signature_request_item_data in self.signature_request:
                signature_request_item = signature_request_item_data.to_dict()

                signature_request.append(signature_request_item)

        signature_response: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.signature_response, Unset):
            signature_response = []
            for signature_response_item_data in self.signature_response:
                signature_response_item = signature_response_item_data.to_dict()

                signature_response.append(signature_response_item)

        state = self.state
        thread_id = self.thread_id
        timing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.timing, Unset):
            timing = self.timing.to_dict()

        trace = self.trace
        transaction_id = self.transaction_id
        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["_type"] = type
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if endorser_write_txn is not UNSET:
            field_dict["endorser_write_txn"] = endorser_write_txn
        if formats is not UNSET:
            field_dict["formats"] = formats
        if messages_attach is not UNSET:
            field_dict["messages_attach"] = messages_attach
        if signature_request is not UNSET:
            field_dict["signature_request"] = signature_request
        if signature_response is not UNSET:
            field_dict["signature_response"] = signature_response
        if state is not UNSET:
            field_dict["state"] = state
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if timing is not UNSET:
            field_dict["timing"] = timing
        if trace is not UNSET:
            field_dict["trace"] = trace
        if transaction_id is not UNSET:
            field_dict["transaction_id"] = transaction_id
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("_type", UNSET)

        connection_id = d.pop("connection_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        endorser_write_txn = d.pop("endorser_write_txn", UNSET)

        formats = []
        _formats = d.pop("formats", UNSET)
        for formats_item_data in _formats or []:
            formats_item = TransactionRecordFormatsItem.from_dict(formats_item_data)

            formats.append(formats_item)

        messages_attach = []
        _messages_attach = d.pop("messages_attach", UNSET)
        for messages_attach_item_data in _messages_attach or []:
            messages_attach_item = TransactionRecordMessagesAttachItem.from_dict(messages_attach_item_data)

            messages_attach.append(messages_attach_item)

        signature_request = []
        _signature_request = d.pop("signature_request", UNSET)
        for signature_request_item_data in _signature_request or []:
            signature_request_item = TransactionRecordSignatureRequestItem.from_dict(signature_request_item_data)

            signature_request.append(signature_request_item)

        signature_response = []
        _signature_response = d.pop("signature_response", UNSET)
        for signature_response_item_data in _signature_response or []:
            signature_response_item = TransactionRecordSignatureResponseItem.from_dict(signature_response_item_data)

            signature_response.append(signature_response_item)

        state = d.pop("state", UNSET)

        thread_id = d.pop("thread_id", UNSET)

        _timing = d.pop("timing", UNSET)
        timing: Union[Unset, TransactionRecordTiming]
        if isinstance(_timing, Unset):
            timing = UNSET
        else:
            timing = TransactionRecordTiming.from_dict(_timing)

        trace = d.pop("trace", UNSET)

        transaction_id = d.pop("transaction_id", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        transaction_record = cls(
            type=type,
            connection_id=connection_id,
            created_at=created_at,
            endorser_write_txn=endorser_write_txn,
            formats=formats,
            messages_attach=messages_attach,
            signature_request=signature_request,
            signature_response=signature_response,
            state=state,
            thread_id=thread_id,
            timing=timing,
            trace=trace,
            transaction_id=transaction_id,
            updated_at=updated_at,
        )

        transaction_record.additional_properties = d
        return transaction_record

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
