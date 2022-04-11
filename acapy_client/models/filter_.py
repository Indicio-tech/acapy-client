from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.filter_const_type_5 import FilterConstType5
from ..models.filter_enum_item import FilterEnumItem
from ..models.filter_exclusive_maximum import FilterExclusiveMaximum
from ..models.filter_exclusive_minimum import FilterExclusiveMinimum
from ..models.filter_maximum import FilterMaximum
from ..models.filter_minimum import FilterMinimum
from ..types import UNSET, Unset

T = TypeVar("T", bound="Filter")


@attr.s(auto_attribs=True)
class Filter:
    """
    Attributes:
        const (Union[FilterConstType5, List[Any], Unset, bool, float, int, str]): Const
        enum (Union[Unset, List[FilterEnumItem]]):
        exclusive_maximum (Union[Unset, FilterExclusiveMaximum]): ExclusiveMaximum
        exclusive_minimum (Union[Unset, FilterExclusiveMinimum]): ExclusiveMinimum
        format_ (Union[Unset, str]): Format
        max_length (Union[Unset, int]): Max Length Example: 1234.
        maximum (Union[Unset, FilterMaximum]): Maximum
        min_length (Union[Unset, int]): Min Length Example: 1234.
        minimum (Union[Unset, FilterMinimum]): Minimum
        not_ (Union[Unset, bool]): Not
        pattern (Union[Unset, str]): Pattern
        type (Union[Unset, str]): Type
    """

    const: Union[FilterConstType5, List[Any], Unset, bool, float, int, str] = UNSET
    enum: Union[Unset, List[FilterEnumItem]] = UNSET
    exclusive_maximum: Union[Unset, FilterExclusiveMaximum] = UNSET
    exclusive_minimum: Union[Unset, FilterExclusiveMinimum] = UNSET
    format_: Union[Unset, str] = UNSET
    max_length: Union[Unset, int] = UNSET
    maximum: Union[Unset, FilterMaximum] = UNSET
    min_length: Union[Unset, int] = UNSET
    minimum: Union[Unset, FilterMinimum] = UNSET
    not_: Union[Unset, bool] = UNSET
    pattern: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        const: Union[Dict[str, Any], List[Any], Unset, bool, float, int, str]
        if isinstance(self.const, Unset):
            const = UNSET

        elif isinstance(self.const, list):
            const = UNSET
            if not isinstance(self.const, Unset):
                const = self.const

        elif isinstance(self.const, FilterConstType5):
            const = UNSET
            if not isinstance(self.const, Unset):
                const = self.const.to_dict()

        else:
            const = self.const

        enum: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.enum, Unset):
            enum = []
            for enum_item_data in self.enum:
                enum_item = enum_item_data.to_dict()

                enum.append(enum_item)

        exclusive_maximum: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.exclusive_maximum, Unset):
            exclusive_maximum = self.exclusive_maximum.to_dict()

        exclusive_minimum: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.exclusive_minimum, Unset):
            exclusive_minimum = self.exclusive_minimum.to_dict()

        format_ = self.format_
        max_length = self.max_length
        maximum: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.maximum, Unset):
            maximum = self.maximum.to_dict()

        min_length = self.min_length
        minimum: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.minimum, Unset):
            minimum = self.minimum.to_dict()

        not_ = self.not_
        pattern = self.pattern
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if const is not UNSET:
            field_dict["const"] = const
        if enum is not UNSET:
            field_dict["enum"] = enum
        if exclusive_maximum is not UNSET:
            field_dict["exclusiveMaximum"] = exclusive_maximum
        if exclusive_minimum is not UNSET:
            field_dict["exclusiveMinimum"] = exclusive_minimum
        if format_ is not UNSET:
            field_dict["format"] = format_
        if max_length is not UNSET:
            field_dict["maxLength"] = max_length
        if maximum is not UNSET:
            field_dict["maximum"] = maximum
        if min_length is not UNSET:
            field_dict["minLength"] = min_length
        if minimum is not UNSET:
            field_dict["minimum"] = minimum
        if not_ is not UNSET:
            field_dict["not"] = not_
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_const(data: object) -> Union[FilterConstType5, List[Any], Unset, bool, float, int, str]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                const_type_4 = cast(List[Any], data)

                return const_type_4
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _const_type_5 = data
                const_type_5: Union[Unset, FilterConstType5]
                if isinstance(_const_type_5, Unset):
                    const_type_5 = UNSET
                else:
                    const_type_5 = FilterConstType5.from_dict(_const_type_5)

                return const_type_5
            except:  # noqa: E722
                pass
            return cast(Union[FilterConstType5, List[Any], Unset, bool, float, int, str], data)

        const = _parse_const(d.pop("const", UNSET))

        enum = []
        _enum = d.pop("enum", UNSET)
        for enum_item_data in _enum or []:
            enum_item = FilterEnumItem.from_dict(enum_item_data)

            enum.append(enum_item)

        _exclusive_maximum = d.pop("exclusiveMaximum", UNSET)
        exclusive_maximum: Union[Unset, FilterExclusiveMaximum]
        if isinstance(_exclusive_maximum, Unset):
            exclusive_maximum = UNSET
        else:
            exclusive_maximum = FilterExclusiveMaximum.from_dict(_exclusive_maximum)

        _exclusive_minimum = d.pop("exclusiveMinimum", UNSET)
        exclusive_minimum: Union[Unset, FilterExclusiveMinimum]
        if isinstance(_exclusive_minimum, Unset):
            exclusive_minimum = UNSET
        else:
            exclusive_minimum = FilterExclusiveMinimum.from_dict(_exclusive_minimum)

        format_ = d.pop("format", UNSET)

        max_length = d.pop("maxLength", UNSET)

        _maximum = d.pop("maximum", UNSET)
        maximum: Union[Unset, FilterMaximum]
        if isinstance(_maximum, Unset):
            maximum = UNSET
        else:
            maximum = FilterMaximum.from_dict(_maximum)

        min_length = d.pop("minLength", UNSET)

        _minimum = d.pop("minimum", UNSET)
        minimum: Union[Unset, FilterMinimum]
        if isinstance(_minimum, Unset):
            minimum = UNSET
        else:
            minimum = FilterMinimum.from_dict(_minimum)

        not_ = d.pop("not", UNSET)

        pattern = d.pop("pattern", UNSET)

        type = d.pop("type", UNSET)

        filter_ = cls(
            const=const,
            enum=enum,
            exclusive_maximum=exclusive_maximum,
            exclusive_minimum=exclusive_minimum,
            format_=format_,
            max_length=max_length,
            maximum=maximum,
            min_length=min_length,
            minimum=minimum,
            not_=not_,
            pattern=pattern,
            type=type,
        )

        filter_.additional_properties = d
        return filter_

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
