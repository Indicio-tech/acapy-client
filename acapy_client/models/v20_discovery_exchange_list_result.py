from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.v20_discovery_record import V20DiscoveryRecord
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20DiscoveryExchangeListResult")


@attr.s(auto_attribs=True)
class V20DiscoveryExchangeListResult:
    """
    Attributes:
        results (Union[Unset, List[V20DiscoveryRecord]]):
    """

    results: Union[Unset, List[V20DiscoveryRecord]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        results: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.results, Unset):
            results = []
            for results_item_data in self.results:
                results_item = results_item_data.to_dict()

                results.append(results_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if results is not UNSET:
            field_dict["results"] = results

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        results = []
        _results = d.pop("results", UNSET)
        for results_item_data in _results or []:
            results_item = V20DiscoveryRecord.from_dict(results_item_data)

            results.append(results_item)

        v20_discovery_exchange_list_result = cls(
            results=results,
        )

        v20_discovery_exchange_list_result.additional_properties = d
        return v20_discovery_exchange_list_result

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