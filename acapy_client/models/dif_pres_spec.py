from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.dif_pres_spec_record_ids import DIFPresSpecRecordIds
from ..models.dif_pres_spec_reveal_doc import DIFPresSpecRevealDoc
from ..models.presentation_definition import PresentationDefinition
from ..types import UNSET, Unset

T = TypeVar("T", bound="DIFPresSpec")


@attr.s(auto_attribs=True)
class DIFPresSpec:
    """
    Attributes:
        issuer_id (Union[Unset, str]): Issuer identifier to sign the presentation, if different from current public DID
        presentation_definition (Union[Unset, PresentationDefinition]):
        record_ids (Union[Unset, DIFPresSpecRecordIds]): Mapping of input_descriptor id to list of stored W3C credential
            record_id Example: {'<input descriptor id_1>': ['<record id_1>', '<record id_2>'], '<input descriptor id_2>':
            ['<record id>']}.
        reveal_doc (Union[Unset, DIFPresSpecRevealDoc]): reveal doc [JSON-LD frame] dict used to derive the credential
            when selective disclosure is required Example: {'@context': ['https://www.w3.org/2018/credentials/v1',
            'https://w3id.org/security/bbs/v1'], '@explicit': True, '@requireAll': True, 'credentialSubject': {'@explicit':
            True, '@requireAll': True, 'Observation': [{'effectiveDateTime': {}, '@explicit': True, '@requireAll': True}]},
            'issuanceDate': {}, 'issuer': {}, 'type': ['VerifiableCredential', 'LabReport']}.
    """

    issuer_id: Union[Unset, str] = UNSET
    presentation_definition: Union[Unset, PresentationDefinition] = UNSET
    record_ids: Union[Unset, DIFPresSpecRecordIds] = UNSET
    reveal_doc: Union[Unset, DIFPresSpecRevealDoc] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issuer_id = self.issuer_id
        presentation_definition: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.presentation_definition, Unset):
            presentation_definition = self.presentation_definition.to_dict()

        record_ids: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.record_ids, Unset):
            record_ids = self.record_ids.to_dict()

        reveal_doc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reveal_doc, Unset):
            reveal_doc = self.reveal_doc.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issuer_id is not UNSET:
            field_dict["issuer_id"] = issuer_id
        if presentation_definition is not UNSET:
            field_dict["presentation_definition"] = presentation_definition
        if record_ids is not UNSET:
            field_dict["record_ids"] = record_ids
        if reveal_doc is not UNSET:
            field_dict["reveal_doc"] = reveal_doc

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        issuer_id = d.pop("issuer_id", UNSET)

        _presentation_definition = d.pop("presentation_definition", UNSET)
        presentation_definition: Union[Unset, PresentationDefinition]
        if isinstance(_presentation_definition, Unset):
            presentation_definition = UNSET
        else:
            presentation_definition = PresentationDefinition.from_dict(_presentation_definition)

        _record_ids = d.pop("record_ids", UNSET)
        record_ids: Union[Unset, DIFPresSpecRecordIds]
        if isinstance(_record_ids, Unset):
            record_ids = UNSET
        else:
            record_ids = DIFPresSpecRecordIds.from_dict(_record_ids)

        _reveal_doc = d.pop("reveal_doc", UNSET)
        reveal_doc: Union[Unset, DIFPresSpecRevealDoc]
        if isinstance(_reveal_doc, Unset):
            reveal_doc = UNSET
        else:
            reveal_doc = DIFPresSpecRevealDoc.from_dict(_reveal_doc)

        dif_pres_spec = cls(
            issuer_id=issuer_id,
            presentation_definition=presentation_definition,
            record_ids=record_ids,
            reveal_doc=reveal_doc,
        )

        dif_pres_spec.additional_properties = d
        return dif_pres_spec

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
