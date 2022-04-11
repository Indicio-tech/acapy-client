from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.connection_metadata_results import ConnectionMetadataResults
from ..types import UNSET, Unset

T = TypeVar("T", bound="ConnectionMetadata")


@attr.s(auto_attribs=True)
class ConnectionMetadata:
    """
    Attributes:
        results (Union[Unset, ConnectionMetadataResults]): Dictionary of metadata associated with connection.
    """

    results: Union[Unset, ConnectionMetadataResults] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.results, Unset):
            results = self.results.to_dict()

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
        results: Union[Unset, ConnectionMetadataResults]
        if isinstance(_results, Unset):
            results = UNSET
        else:
            results = ConnectionMetadataResults.from_dict(_results)

        connection_metadata = cls(
            results=results,
        )

        connection_metadata.additional_properties = d
        return connection_metadata

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
