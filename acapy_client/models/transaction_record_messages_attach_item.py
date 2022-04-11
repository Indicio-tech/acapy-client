from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="TransactionRecordMessagesAttachItem")


@attr.s(auto_attribs=True)
class TransactionRecordMessagesAttachItem:
    """
    Example:
        {'@id': '143c458d-1b1c-40c7-ab85-4d16808ddf0a', 'data': {'json': '{"endorser":
            "V4SGRU86Z58d6TV7PBUe6f","identifier": "LjgpST2rjsoxYegQDRm7EL","operation": {"data": {"attr_names":
            ["first_name", "last_name"],"name": "test_schema","version": "2.1",},"type": "101",},"protocolVersion":
            2,"reqId": 1597766666168851000,"signatures": {"LjgpST2rjsox":
            "4ATKMn6Y9sTgwqaGTm7py2c2M8x1EVDTWKZArwyuPgjU"},"taaAcceptance": {"mechanism": "manual","taaDigest":
            "f50fe2c2ab977006761d36bd6f23e4c6a7e0fc2feb9f62","time": 1597708800,}}'}, 'mime-type': 'application/json'}

    """

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        transaction_record_messages_attach_item = cls()

        transaction_record_messages_attach_item.additional_properties = d
        return transaction_record_messages_attach_item

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
