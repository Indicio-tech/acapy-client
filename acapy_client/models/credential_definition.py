from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.cred_def_value import CredDefValue
from ..models.credential_definition_type import CredentialDefinitionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CredentialDefinition")


@attr.s(auto_attribs=True)
class CredentialDefinition:
    """
    Attributes:
        id (Union[Unset, str]): Credential definition identifier Example: WgWxqztrNooG92RXvxSTWv:3:CL:20:tag.
        schema_id (Union[Unset, str]): Schema identifier within credential definition identifier Example: 20.
        tag (Union[Unset, str]): Tag within credential definition identifier Example: tag.
        type (Union[Unset, CredentialDefinitionType]): Signature type: CL for Camenisch-Lysyanskaya Example: CL.
        value (Union[Unset, CredDefValue]):
        ver (Union[Unset, str]): Node protocol version Example: 1.0.
    """

    id: Union[Unset, str] = UNSET
    schema_id: Union[Unset, str] = UNSET
    tag: Union[Unset, str] = UNSET
    type: Union[Unset, CredentialDefinitionType] = UNSET
    value: Union[Unset, CredDefValue] = UNSET
    ver: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        schema_id = self.schema_id
        tag = self.tag
        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        ver = self.ver

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if schema_id is not UNSET:
            field_dict["schemaId"] = schema_id
        if tag is not UNSET:
            field_dict["tag"] = tag
        if type is not UNSET:
            field_dict["type"] = type
        if value is not UNSET:
            field_dict["value"] = value
        if ver is not UNSET:
            field_dict["ver"] = ver

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        schema_id = d.pop("schemaId", UNSET)

        tag = d.pop("tag", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CredentialDefinitionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CredentialDefinitionType.from_dict(_type)

        _value = d.pop("value", UNSET)
        value: Union[Unset, CredDefValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = CredDefValue.from_dict(_value)

        ver = d.pop("ver", UNSET)

        credential_definition = cls(
            id=id,
            schema_id=schema_id,
            tag=tag,
            type=type,
            value=value,
            ver=ver,
        )

        credential_definition.additional_properties = d
        return credential_definition

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
