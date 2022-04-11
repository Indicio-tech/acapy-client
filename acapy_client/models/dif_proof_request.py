from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.dif_options import DIFOptions
from ..models.presentation_definition import PresentationDefinition
from ..types import UNSET, Unset

T = TypeVar("T", bound="DIFProofRequest")


@attr.s(auto_attribs=True)
class DIFProofRequest:
    """
    Attributes:
        presentation_definition (PresentationDefinition):
        options (Union[Unset, DIFOptions]):
    """

    presentation_definition: PresentationDefinition
    options: Union[Unset, DIFOptions] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        presentation_definition = self.presentation_definition.to_dict()

        options: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "presentation_definition": presentation_definition,
            }
        )
        if options is not UNSET:
            field_dict["options"] = options

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        presentation_definition = PresentationDefinition.from_dict(d.pop("presentation_definition"))

        _options = d.pop("options", UNSET)
        options: Union[Unset, DIFOptions]
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = DIFOptions.from_dict(_options)

        dif_proof_request = cls(
            presentation_definition=presentation_definition,
            options=options,
        )

        dif_proof_request.additional_properties = d
        return dif_proof_request

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
