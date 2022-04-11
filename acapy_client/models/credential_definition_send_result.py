from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CredentialDefinitionSendResult")


@attr.s(auto_attribs=True)
class CredentialDefinitionSendResult:
    """
    Attributes:
        credential_definition_id (str): Credential definition identifier Example: WgWxqztrNooG92RXvxSTWv:3:CL:20:tag.
    """

    credential_definition_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credential_definition_id = self.credential_definition_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credential_definition_id": credential_definition_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credential_definition_id = d.pop("credential_definition_id")

        credential_definition_send_result = cls(
            credential_definition_id=credential_definition_id,
        )

        credential_definition_send_result.additional_properties = d
        return credential_definition_send_result

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
