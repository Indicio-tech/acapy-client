from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.dif_options import DIFOptions
from ..models.input_descriptors import InputDescriptors
from ..types import UNSET, Unset

T = TypeVar("T", bound="DIFProofProposal")


@attr.s(auto_attribs=True)
class DIFProofProposal:
    """
    Attributes:
        input_descriptors (Union[Unset, List[InputDescriptors]]):
        options (Union[Unset, DIFOptions]):
    """

    input_descriptors: Union[Unset, List[InputDescriptors]] = UNSET
    options: Union[Unset, DIFOptions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        input_descriptors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.input_descriptors, Unset):
            input_descriptors = []
            for input_descriptors_item_data in self.input_descriptors:
                input_descriptors_item = input_descriptors_item_data.to_dict()

                input_descriptors.append(input_descriptors_item)

        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_descriptors is not UNSET:
            field_dict["input_descriptors"] = input_descriptors
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        input_descriptors = []
        _input_descriptors = d.pop("input_descriptors", UNSET)
        for input_descriptors_item_data in _input_descriptors or []:
            input_descriptors_item = InputDescriptors.from_dict(input_descriptors_item_data)

            input_descriptors.append(input_descriptors_item)

        _options = d.pop("options", UNSET)
        options: Union[Unset, DIFOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = DIFOptions.from_dict(_options)

        dif_proof_proposal = cls(
            input_descriptors=input_descriptors,
            options=options,
        )

        dif_proof_proposal.additional_properties = d
        return dif_proof_proposal

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
