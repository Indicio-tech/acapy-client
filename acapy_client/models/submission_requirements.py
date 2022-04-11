from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.submission_requirements_from_nested_item import SubmissionRequirementsFromNestedItem
from ..models.submission_requirements_rule import SubmissionRequirementsRule
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubmissionRequirements")


@attr.s(auto_attribs=True)
class SubmissionRequirements:
    """
    Attributes:
        count (Union[Unset, int]): Count Value Example: 1234.
        from_ (Union[Unset, str]): From
        from_nested (Union[Unset, List[SubmissionRequirementsFromNestedItem]]):
        max_ (Union[Unset, int]): Max Value Example: 1234.
        min_ (Union[Unset, int]): Min Value Example: 1234.
        name (Union[Unset, str]): Name
        purpose (Union[Unset, str]): Purpose
        rule (Union[Unset, SubmissionRequirementsRule]): Selection
    """

    count: Union[Unset, int] = UNSET
    from_: Union[Unset, str] = UNSET
    from_nested: Union[Unset, List[SubmissionRequirementsFromNestedItem]] = UNSET
    max_: Union[Unset, int] = UNSET
    min_: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    purpose: Union[Unset, str] = UNSET
    rule: Union[Unset, SubmissionRequirementsRule] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        from_ = self.from_
        from_nested: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.from_nested, Unset):
            from_nested = []
            for from_nested_item_data in self.from_nested:
                from_nested_item = from_nested_item_data.to_dict()

                from_nested.append(from_nested_item)

        max_ = self.max_
        min_ = self.min_
        name = self.name
        purpose = self.purpose
        rule: Union[Unset, str] = UNSET
        if not isinstance(self.rule, Unset):
            rule = self.rule.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if from_ is not UNSET:
            field_dict["from"] = from_
        if from_nested is not UNSET:
            field_dict["from_nested"] = from_nested
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if name is not UNSET:
            field_dict["name"] = name
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if rule is not UNSET:
            field_dict["rule"] = rule

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count", UNSET)

        from_ = d.pop("from", UNSET)

        from_nested = []
        _from_nested = d.pop("from_nested", UNSET)
        for from_nested_item_data in _from_nested or []:
            from_nested_item = SubmissionRequirementsFromNestedItem.from_dict(from_nested_item_data)

            from_nested.append(from_nested_item)

        max_ = d.pop("max", UNSET)

        min_ = d.pop("min", UNSET)

        name = d.pop("name", UNSET)

        purpose = d.pop("purpose", UNSET)

        _rule = d.pop("rule", UNSET)
        rule: Union[Unset, SubmissionRequirementsRule]
        if isinstance(_rule, Unset):
            rule = UNSET
        else:
            rule = SubmissionRequirementsRule(_rule)

        submission_requirements = cls(
            count=count,
            from_=from_,
            from_nested=from_nested,
            max_=max_,
            min_=min_,
            name=name,
            purpose=purpose,
            rule=rule,
        )

        submission_requirements.additional_properties = d
        return submission_requirements

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
