from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="V10CredentialProblemReportRequest")


@attr.s(auto_attribs=True)
class V10CredentialProblemReportRequest:
    """
    Attributes:
        description (str):
    """

    description: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description")

        v10_credential_problem_report_request = cls(
            description=description,
        )

        v10_credential_problem_report_request.additional_properties = d
        return v10_credential_problem_report_request

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
