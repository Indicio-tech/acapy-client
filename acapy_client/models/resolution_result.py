from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.resolution_result_did_doc import ResolutionResultDidDoc
from ..models.resolution_result_metadata import ResolutionResultMetadata

T = TypeVar("T", bound="ResolutionResult")


@attr.s(auto_attribs=True)
class ResolutionResult:
    """
    Attributes:
        did_doc (ResolutionResultDidDoc): DID Document
        metadata (ResolutionResultMetadata): Resolution metadata
    """

    did_doc: ResolutionResultDidDoc
    metadata: ResolutionResultMetadata
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        did_doc = self.did_doc.to_dict()

        metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "did_doc": did_doc,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        did_doc = ResolutionResultDidDoc.from_dict(d.pop("did_doc"))

        metadata = ResolutionResultMetadata.from_dict(d.pop("metadata"))

        resolution_result = cls(
            did_doc=did_doc,
            metadata=metadata,
        )

        resolution_result.additional_properties = d
        return resolution_result

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
