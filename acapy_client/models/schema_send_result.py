from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.schema import Schema

T = TypeVar("T", bound="SchemaSendResult")


@attr.s(auto_attribs=True)
class SchemaSendResult:
    """
    Attributes:
        schema (Schema):
        schema_id (str): Schema identifier Example: WgWxqztrNooG92RXvxSTWv:2:schema_name:1.0.
    """

    schema: Schema
    schema_id: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        schema = self.schema.to_dict()

        schema_id = self.schema_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "schema": schema,
                "schema_id": schema_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        schema = Schema.from_dict(d.pop("schema"))

        schema_id = d.pop("schema_id")

        schema_send_result = cls(
            schema=schema,
            schema_id=schema_id,
        )

        schema_send_result.additional_properties = d
        return schema_send_result

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
