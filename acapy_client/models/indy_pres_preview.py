from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_pres_attr_spec import IndyPresAttrSpec
from ..models.indy_pres_pred_spec import IndyPresPredSpec
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyPresPreview")


@attr.s(auto_attribs=True)
class IndyPresPreview:
    """
    Attributes:
        attributes (List[IndyPresAttrSpec]):
        predicates (List[IndyPresPredSpec]):
        type (Union[Unset, str]): Message type identifier Example: did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/present-
            proof/1.0/presentation-preview.
    """

    attributes: List[IndyPresAttrSpec]
    predicates: List[IndyPresPredSpec]
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes = []
        for attributes_item_data in self.attributes:
            attributes_item = attributes_item_data.to_dict()

            attributes.append(attributes_item)

        predicates = []
        for predicates_item_data in self.predicates:
            predicates_item = predicates_item_data.to_dict()

            predicates.append(predicates_item)

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "attributes": attributes,
                "predicates": predicates,
            }
        )
        if type is not UNSET:
            field_dict["@type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attributes = []
        _attributes = d.pop("attributes")
        for attributes_item_data in _attributes:
            attributes_item = IndyPresAttrSpec.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        predicates = []
        _predicates = d.pop("predicates")
        for predicates_item_data in _predicates:
            predicates_item = IndyPresPredSpec.from_dict(predicates_item_data)

            predicates.append(predicates_item)

        type = d.pop("@type", UNSET)

        indy_pres_preview = cls(
            attributes=attributes,
            predicates=predicates,
            type=type,
        )

        indy_pres_preview.additional_properties = d
        return indy_pres_preview

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
