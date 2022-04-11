from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attribute_mime_types_result_results import AttributeMimeTypesResultResults
from ..types import UNSET, Unset

T = TypeVar("T", bound="AttributeMimeTypesResult")


@attr.s(auto_attribs=True)
class AttributeMimeTypesResult:
    """
    Attributes:
        results (Union[Unset, None, AttributeMimeTypesResultResults]):
    """

    results: Union[Unset, None, AttributeMimeTypesResultResults] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results.to_dict() if self.results else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _results = d.pop("results", UNSET)
        results: Union[Unset, None, AttributeMimeTypesResultResults]
        if _results is None:
            results = None
        elif isinstance(_results, Unset):
            results = UNSET
        else:
            results = AttributeMimeTypesResultResults.from_dict(_results)

        attribute_mime_types_result = cls(
            results=results,
        )

        attribute_mime_types_result.additional_properties = d
        return attribute_mime_types_result

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
