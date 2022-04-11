from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="V20PresFormat")


@attr.s(auto_attribs=True)
class V20PresFormat:
    """
    Attributes:
        attach_id (str): Attachment identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        format_ (str): Attachment format specifier Example: dif/presentation-exchange/submission@v1.0.
    """

    attach_id: str
    format_: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attach_id = self.attach_id
        format_ = self.format_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attach_id": attach_id,
                "format": format_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attach_id = d.pop("attach_id")

        format_ = d.pop("format")

        v20_pres_format = cls(
            attach_id=attach_id,
            format_=format_,
        )

        v20_pres_format.additional_properties = d
        return v20_pres_format

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
