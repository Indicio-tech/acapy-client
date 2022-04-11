from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.w3c_credentials_list_request_tag_query import W3CCredentialsListRequestTagQuery
from ..types import UNSET, Unset

T = TypeVar("T", bound="W3CCredentialsListRequest")


@attr.s(auto_attribs=True)
class W3CCredentialsListRequest:
    """
    Attributes:
        contexts (Union[Unset, List[str]]):
        given_id (Union[Unset, str]): Given credential id to match
        issuer_id (Union[Unset, str]): Credential issuer identifier to match
        max_results (Union[Unset, int]): Maximum number of results to return
        proof_types (Union[Unset, List[str]]):
        schema_ids (Union[Unset, List[str]]): Schema identifiers, all of which to match
        subject_ids (Union[Unset, List[str]]): Subject identifiers, all of which to match
        tag_query (Union[Unset, W3CCredentialsListRequestTagQuery]): Tag filter
        types (Union[Unset, List[str]]):
    """

    contexts: Union[Unset, List[str]] = UNSET
    given_id: Union[Unset, str] = UNSET
    issuer_id: Union[Unset, str] = UNSET
    max_results: Union[Unset, int] = UNSET
    proof_types: Union[Unset, List[str]] = UNSET
    schema_ids: Union[Unset, List[str]] = UNSET
    subject_ids: Union[Unset, List[str]] = UNSET
    tag_query: Union[Unset, W3CCredentialsListRequestTagQuery] = UNSET
    types: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contexts: Union[Unset, List[str]] = UNSET
        if not isinstance(self.contexts, Unset):
            contexts = self.contexts

        given_id = self.given_id
        issuer_id = self.issuer_id
        max_results = self.max_results
        proof_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.proof_types, Unset):
            proof_types = self.proof_types

        schema_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.schema_ids, Unset):
            schema_ids = self.schema_ids

        subject_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.subject_ids, Unset):
            subject_ids = self.subject_ids

        tag_query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tag_query, Unset):
            tag_query = self.tag_query.to_dict()

        types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.types, Unset):
            types = self.types

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contexts is not UNSET:
            field_dict["contexts"] = contexts
        if given_id is not UNSET:
            field_dict["given_id"] = given_id
        if issuer_id is not UNSET:
            field_dict["issuer_id"] = issuer_id
        if max_results is not UNSET:
            field_dict["max_results"] = max_results
        if proof_types is not UNSET:
            field_dict["proof_types"] = proof_types
        if schema_ids is not UNSET:
            field_dict["schema_ids"] = schema_ids
        if subject_ids is not UNSET:
            field_dict["subject_ids"] = subject_ids
        if tag_query is not UNSET:
            field_dict["tag_query"] = tag_query
        if types is not UNSET:
            field_dict["types"] = types

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contexts = cast(List[str], d.pop("contexts", UNSET))

        given_id = d.pop("given_id", UNSET)

        issuer_id = d.pop("issuer_id", UNSET)

        max_results = d.pop("max_results", UNSET)

        proof_types = cast(List[str], d.pop("proof_types", UNSET))

        schema_ids = cast(List[str], d.pop("schema_ids", UNSET))

        subject_ids = cast(List[str], d.pop("subject_ids", UNSET))

        _tag_query = d.pop("tag_query", UNSET)
        tag_query: Union[Unset, W3CCredentialsListRequestTagQuery]
        if isinstance(_tag_query, Unset):
            tag_query = UNSET
        else:
            tag_query = W3CCredentialsListRequestTagQuery.from_dict(_tag_query)

        types = cast(List[str], d.pop("types", UNSET))

        w3c_credentials_list_request = cls(
            contexts=contexts,
            given_id=given_id,
            issuer_id=issuer_id,
            max_results=max_results,
            proof_types=proof_types,
            schema_ids=schema_ids,
            subject_ids=subject_ids,
            tag_query=tag_query,
            types=types,
        )

        w3c_credentials_list_request.additional_properties = d
        return w3c_credentials_list_request

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
