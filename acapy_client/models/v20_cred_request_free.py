from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.v20_cred_filter_ld_proof import V20CredFilterLDProof
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20CredRequestFree")


@attr.s(auto_attribs=True)
class V20CredRequestFree:
    """
    Attributes:
        connection_id (str): Connection identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        filter_ (V20CredFilterLDProof):
        auto_remove (Union[Unset, bool]): Whether to remove the credential exchange record on completion (overrides
            --preserve-exchange-records configuration setting)
        comment (Union[Unset, None, str]): Human-readable comment
        holder_did (Union[Unset, None, str]): Holder DID to substitute for the credentialSubject.id Example:
            did:key:ahsdkjahsdkjhaskjdhakjshdkajhsdkjahs.
        trace (Union[Unset, bool]): Whether to trace event (default false)
    """

    connection_id: str
    filter_: V20CredFilterLDProof
    auto_remove: Union[Unset, bool] = UNSET
    comment: Union[Unset, None, str] = UNSET
    holder_did: Union[Unset, None, str] = UNSET
    trace: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id
        filter_ = self.filter_.to_dict()

        auto_remove = self.auto_remove
        comment = self.comment
        holder_did = self.holder_did
        trace = self.trace

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connection_id": connection_id,
                "filter": filter_,
            }
        )
        if auto_remove is not UNSET:
            field_dict["auto_remove"] = auto_remove
        if comment is not UNSET:
            field_dict["comment"] = comment
        if holder_did is not UNSET:
            field_dict["holder_did"] = holder_did
        if trace is not UNSET:
            field_dict["trace"] = trace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connection_id")

        filter_ = V20CredFilterLDProof.from_dict(d.pop("filter"))

        auto_remove = d.pop("auto_remove", UNSET)

        comment = d.pop("comment", UNSET)

        holder_did = d.pop("holder_did", UNSET)

        trace = d.pop("trace", UNSET)

        v20_cred_request_free = cls(
            connection_id=connection_id,
            filter_=filter_,
            auto_remove=auto_remove,
            comment=comment,
            holder_did=holder_did,
            trace=trace,
        )

        v20_cred_request_free.additional_properties = d
        return v20_cred_request_free

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
