from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.vc_record_cred_tags import VCRecordCredTags
from ..models.vc_record_cred_value import VCRecordCredValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="VCRecord")


@attr.s(auto_attribs=True)
class VCRecord:
    """
    Attributes:
        contexts (Union[Unset, List[str]]):
        cred_tags (Union[Unset, VCRecordCredTags]):
        cred_value (Union[Unset, VCRecordCredValue]): (JSON-serializable) credential value
        expanded_types (Union[Unset, List[str]]):
        given_id (Union[Unset, str]): Credential identifier Example: http://example.edu/credentials/3732.
        issuer_id (Union[Unset, str]): Issuer identifier Example: https://example.edu/issuers/14.
        proof_types (Union[Unset, List[str]]):
        record_id (Union[Unset, str]): Record identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        schema_ids (Union[Unset, List[str]]):
        subject_ids (Union[Unset, List[str]]):
    """

    contexts: Union[Unset, List[str]] = UNSET
    cred_tags: Union[Unset, VCRecordCredTags] = UNSET
    cred_value: Union[Unset, VCRecordCredValue] = UNSET
    expanded_types: Union[Unset, List[str]] = UNSET
    given_id: Union[Unset, str] = UNSET
    issuer_id: Union[Unset, str] = UNSET
    proof_types: Union[Unset, List[str]] = UNSET
    record_id: Union[Unset, str] = UNSET
    schema_ids: Union[Unset, List[str]] = UNSET
    subject_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contexts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.contexts, Unset):
            contexts = self.contexts

        cred_tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cred_tags, Unset):
            cred_tags = self.cred_tags.to_dict()

        cred_value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cred_value, Unset):
            cred_value = self.cred_value.to_dict()

        expanded_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.expanded_types, Unset):
            expanded_types = self.expanded_types

        given_id = self.given_id
        issuer_id = self.issuer_id
        proof_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.proof_types, Unset):
            proof_types = self.proof_types

        record_id = self.record_id
        schema_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.schema_ids, Unset):
            schema_ids = self.schema_ids

        subject_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subject_ids, Unset):
            subject_ids = self.subject_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contexts is not UNSET:
            field_dict["contexts"] = contexts
        if cred_tags is not UNSET:
            field_dict["cred_tags"] = cred_tags
        if cred_value is not UNSET:
            field_dict["cred_value"] = cred_value
        if expanded_types is not UNSET:
            field_dict["expanded_types"] = expanded_types
        if given_id is not UNSET:
            field_dict["given_id"] = given_id
        if issuer_id is not UNSET:
            field_dict["issuer_id"] = issuer_id
        if proof_types is not UNSET:
            field_dict["proof_types"] = proof_types
        if record_id is not UNSET:
            field_dict["record_id"] = record_id
        if schema_ids is not UNSET:
            field_dict["schema_ids"] = schema_ids
        if subject_ids is not UNSET:
            field_dict["subject_ids"] = subject_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contexts = cast(List[str], d.pop("contexts", UNSET))

        _cred_tags = d.pop("cred_tags", UNSET)
        cred_tags: Union[Unset, VCRecordCredTags]
        if isinstance(_cred_tags, Unset):
            cred_tags = UNSET
        else:
            cred_tags = VCRecordCredTags.from_dict(_cred_tags)

        _cred_value = d.pop("cred_value", UNSET)
        cred_value: Union[Unset, VCRecordCredValue]
        if isinstance(_cred_value, Unset):
            cred_value = UNSET
        else:
            cred_value = VCRecordCredValue.from_dict(_cred_value)

        expanded_types = cast(List[str], d.pop("expanded_types", UNSET))

        given_id = d.pop("given_id", UNSET)

        issuer_id = d.pop("issuer_id", UNSET)

        proof_types = cast(List[str], d.pop("proof_types", UNSET))

        record_id = d.pop("record_id", UNSET)

        schema_ids = cast(List[str], d.pop("schema_ids", UNSET))

        subject_ids = cast(List[str], d.pop("subject_ids", UNSET))

        vc_record = cls(
            contexts=contexts,
            cred_tags=cred_tags,
            cred_value=cred_value,
            expanded_types=expanded_types,
            given_id=given_id,
            issuer_id=issuer_id,
            proof_types=proof_types,
            record_id=record_id,
            schema_ids=schema_ids,
            subject_ids=subject_ids,
        )

        vc_record.additional_properties = d
        return vc_record

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
