from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.filter_const_type_5 import FilterConstType5
from ..models.filter_enum_item import FilterEnumItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="Filter")


@attr.s(auto_attribs=True)
class Filter:
    """ """

    const: Union[FilterConstType5, List[Any], Unset, bool, float, int, str] = UNSET
    enum: Union[Unset, List[FilterEnumItem]] = UNSET
    exclusive_maximum: Union[Unset, float, str] = UNSET
    exclusive_minimum: Union[Unset, float, str] = UNSET
    format_: Union[Unset, str] = UNSET
    max_length: Union[Unset, int] = UNSET
    maximum: Union[Unset, float, str] = UNSET
    min_length: Union[Unset, int] = UNSET
    minimum: Union[Unset, float, str] = UNSET
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
                const = []
                for const_type_4_item_data in self.const:
                    const_type_4_item = const_type_4_item_data

                    const.append(const_type_4_item)

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

        exclusive_maximum: Union[Unset, float, str]
        if isinstance(self.exclusive_maximum, Unset):
            exclusive_maximum = UNSET
        else:
            exclusive_maximum = self.exclusive_maximum

        exclusive_minimum: Union[Unset, float, str]
        if isinstance(self.exclusive_minimum, Unset):
            exclusive_minimum = UNSET
        else:
            exclusive_minimum = self.exclusive_minimum

        format_ = self.format_
        max_length = self.max_length
        maximum: Union[Unset, float, str]
        if isinstance(self.maximum, Unset):
            maximum = UNSET
        else:
            maximum = self.maximum

        min_length = self.min_length
        minimum: Union[Unset, float, str]
        if isinstance(self.minimum, Unset):
            minimum = UNSET
        else:
            minimum = self.minimum

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
                const_type_4 = UNSET
                _const_type_4 = data
                for const_type_4_item_data in _const_type_4 or []:
                    const_type_4_item = const_type_4_item_data

                    const_type_4.append(const_type_4_item)

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

        def _parse_exclusive_maximum(data: object) -> Union[Unset, float, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, float, str], data)

        exclusive_maximum = _parse_exclusive_maximum(d.pop("exclusiveMaximum", UNSET))

        def _parse_exclusive_minimum(data: object) -> Union[Unset, float, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, float, str], data)

        exclusive_minimum = _parse_exclusive_minimum(d.pop("exclusiveMinimum", UNSET))

        format_ = d.pop("format", UNSET)

        max_length = d.pop("maxLength", UNSET)

        def _parse_maximum(data: object) -> Union[Unset, float, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, float, str], data)

        maximum = _parse_maximum(d.pop("maximum", UNSET))

        min_length = d.pop("minLength", UNSET)

        def _parse_minimum(data: object) -> Union[Unset, float, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, float, str], data)

        minimum = _parse_minimum(d.pop("minimum", UNSET))

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
