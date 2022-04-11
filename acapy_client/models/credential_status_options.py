from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="CredentialStatusOptions")


@attr.s(auto_attribs=True)
class CredentialStatusOptions:
    """
    Attributes:
        type (str): Credential status method type to use for the credential. Should match status method registered in
            the Verifiable Credential Extension Registry Example: CredentialStatusList2017.
    """

    type: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = d.pop("type")

        credential_status_options = cls(
            type=type,
        )

        credential_status_options.additional_properties = d
        return credential_status_options

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
