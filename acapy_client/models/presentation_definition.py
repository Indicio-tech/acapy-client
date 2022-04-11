from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.claim_format import ClaimFormat
from ..models.input_descriptors import InputDescriptors
from ..models.submission_requirements import SubmissionRequirements
from ..types import UNSET, Unset

T = TypeVar("T", bound="PresentationDefinition")


@attr.s(auto_attribs=True)
class PresentationDefinition:
    """
    Attributes:
        format_ (Union[Unset, ClaimFormat]):
        id (Union[Unset, str]): Unique Resource Identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        input_descriptors (Union[Unset, List[InputDescriptors]]):
        name (Union[Unset, str]): Human-friendly name that describes what the presentation definition pertains to
        purpose (Union[Unset, str]): Describes the purpose for which the Presentation Definition's inputs are being
            requested
        submission_requirements (Union[Unset, List[SubmissionRequirements]]):
    """

    format_: Union[Unset, ClaimFormat] = UNSET
    id: Union[Unset, str] = UNSET
    input_descriptors: Union[Unset, List[InputDescriptors]] = UNSET
    name: Union[Unset, str] = UNSET
    purpose: Union[Unset, str] = UNSET
    submission_requirements: Union[Unset, List[SubmissionRequirements]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        format_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.to_dict()

        id = self.id
        input_descriptors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.input_descriptors, Unset):
            input_descriptors = []
            for input_descriptors_item_data in self.input_descriptors:
                input_descriptors_item = input_descriptors_item_data.to_dict()

                input_descriptors.append(input_descriptors_item)

        name = self.name
        purpose = self.purpose
        submission_requirements: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.submission_requirements, Unset):
            submission_requirements = []
            for submission_requirements_item_data in self.submission_requirements:
                submission_requirements_item = submission_requirements_item_data.to_dict()

                submission_requirements.append(submission_requirements_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if format_ is not UNSET:
            field_dict["format"] = format_
        if id is not UNSET:
            field_dict["id"] = id
        if input_descriptors is not UNSET:
            field_dict["input_descriptors"] = input_descriptors
        if name is not UNSET:
            field_dict["name"] = name
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if submission_requirements is not UNSET:
            field_dict["submission_requirements"] = submission_requirements

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, ClaimFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = ClaimFormat.from_dict(_format_)

        id = d.pop("id", UNSET)

        input_descriptors = []
        _input_descriptors = d.pop("input_descriptors", UNSET)
        for input_descriptors_item_data in _input_descriptors or []:
            input_descriptors_item = InputDescriptors.from_dict(input_descriptors_item_data)

            input_descriptors.append(input_descriptors_item)

        name = d.pop("name", UNSET)

        purpose = d.pop("purpose", UNSET)

        submission_requirements = []
        _submission_requirements = d.pop("submission_requirements", UNSET)
        for submission_requirements_item_data in _submission_requirements or []:
            submission_requirements_item = SubmissionRequirements.from_dict(submission_requirements_item_data)

            submission_requirements.append(submission_requirements_item)

        presentation_definition = cls(
            format_=format_,
            id=id,
            input_descriptors=input_descriptors,
            name=name,
            purpose=purpose,
            submission_requirements=submission_requirements,
        )

        presentation_definition.additional_properties = d
        return presentation_definition

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
