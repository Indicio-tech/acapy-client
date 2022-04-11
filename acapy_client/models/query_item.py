from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.query_item_feature_type import QueryItemFeatureType

T = TypeVar("T", bound="QueryItem")


@attr.s(auto_attribs=True)
class QueryItem:
    """
    Attributes:
        feature_type (QueryItemFeatureType): feature type
        match (str): match
    """

    feature_type: QueryItemFeatureType
    match: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        feature_type = self.feature_type.value

        match = self.match

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "feature-type": feature_type,
                "match": match,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        feature_type = QueryItemFeatureType(d.pop("feature-type"))

        match = d.pop("match")

        query_item = cls(
            feature_type=feature_type,
            match=match,
        )

        query_item.additional_properties = d
        return query_item

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
