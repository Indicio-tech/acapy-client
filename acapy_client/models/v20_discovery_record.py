from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.disclosures import Disclosures
from ..models.queries import Queries
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20DiscoveryRecord")


@attr.s(auto_attribs=True)
class V20DiscoveryRecord:
    """
    Attributes:
        connection_id (Union[Unset, str]): Connection identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        created_at (Union[Unset, str]): Time of record creation Example: 2021-12-31 23:59:59+00:00.
        disclosures (Union[Unset, Disclosures]):
        discovery_exchange_id (Union[Unset, str]): Credential exchange identifier Example:
            3fa85f64-5717-4562-b3fc-2c963f66afa6.
        queries_msg (Union[Unset, Queries]):
        state (Union[Unset, str]): Current record state Example: active.
        thread_id (Union[Unset, str]): Thread identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        trace (Union[Unset, bool]): Record trace information, based on agent configuration
        updated_at (Union[Unset, str]): Time of last record update Example: 2021-12-31 23:59:59+00:00.
    """

    connection_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    disclosures: Union[Unset, Disclosures] = UNSET
    discovery_exchange_id: Union[Unset, str] = UNSET
    queries_msg: Union[Unset, Queries] = UNSET
    state: Union[Unset, str] = UNSET
    thread_id: Union[Unset, str] = UNSET
    trace: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id
        created_at = self.created_at
        disclosures: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.disclosures, Unset):
            disclosures = self.disclosures.to_dict()

        discovery_exchange_id = self.discovery_exchange_id
        queries_msg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.queries_msg, Unset):
            queries_msg = self.queries_msg.to_dict()

        state = self.state
        thread_id = self.thread_id
        trace = self.trace
        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connection_id is not UNSET:
            field_dict["connection_id"] = connection_id
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if disclosures is not UNSET:
            field_dict["disclosures"] = disclosures
        if discovery_exchange_id is not UNSET:
            field_dict["discovery_exchange_id"] = discovery_exchange_id
        if queries_msg is not UNSET:
            field_dict["queries_msg"] = queries_msg
        if state is not UNSET:
            field_dict["state"] = state
        if thread_id is not UNSET:
            field_dict["thread_id"] = thread_id
        if trace is not UNSET:
            field_dict["trace"] = trace
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        connection_id = d.pop("connection_id", UNSET)

        created_at = d.pop("created_at", UNSET)

        _disclosures = d.pop("disclosures", UNSET)
        disclosures: Union[Unset, Disclosures]
        if isinstance(_disclosures, Unset):
            disclosures = UNSET
        else:
            disclosures = Disclosures.from_dict(_disclosures)

        discovery_exchange_id = d.pop("discovery_exchange_id", UNSET)

        _queries_msg = d.pop("queries_msg", UNSET)
        queries_msg: Union[Unset, Queries]
        if isinstance(_queries_msg, Unset):
            queries_msg = UNSET
        else:
            queries_msg = Queries.from_dict(_queries_msg)

        state = d.pop("state", UNSET)

        thread_id = d.pop("thread_id", UNSET)

        trace = d.pop("trace", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        v20_discovery_record = cls(
            connection_id=connection_id,
            created_at=created_at,
            disclosures=disclosures,
            discovery_exchange_id=discovery_exchange_id,
            queries_msg=queries_msg,
            state=state,
            thread_id=thread_id,
            trace=trace,
            updated_at=updated_at,
        )

        v20_discovery_record.additional_properties = d
        return v20_discovery_record

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
