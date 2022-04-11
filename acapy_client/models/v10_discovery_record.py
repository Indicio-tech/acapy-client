from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.disclose import Disclose
from ..models.query import Query
from ..types import UNSET, Unset

T = TypeVar("T", bound="V10DiscoveryRecord")


@attr.s(auto_attribs=True)
class V10DiscoveryRecord:
    """
    Attributes:
        connection_id (Union[Unset, str]): Connection identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        created_at (Union[Unset, str]): Time of record creation Example: 2021-12-31 23:59:59+00:00.
        disclose (Union[Unset, Disclose]):
        discovery_exchange_id (Union[Unset, str]): Credential exchange identifier Example:
            3fa85f64-5717-4562-b3fc-2c963f66afa6.
        query_msg (Union[Unset, Query]):
        state (Union[Unset, str]): Current record state Example: active.
        thread_id (Union[Unset, str]): Thread identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        trace (Union[Unset, bool]): Record trace information, based on agent configuration
        updated_at (Union[Unset, str]): Time of last record update Example: 2021-12-31 23:59:59+00:00.
    """

    connection_id: Union[Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    disclose: Union[Unset, Disclose] = UNSET
    discovery_exchange_id: Union[Unset, str] = UNSET
    query_msg: Union[Unset, Query] = UNSET
    state: Union[Unset, str] = UNSET
    thread_id: Union[Unset, str] = UNSET
    trace: Union[Unset, bool] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        connection_id = self.connection_id
        created_at = self.created_at
        disclose: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.disclose, Unset):
            disclose = self.disclose.to_dict()

        discovery_exchange_id = self.discovery_exchange_id
        query_msg: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query_msg, Unset):
            query_msg = self.query_msg.to_dict()

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
        if disclose is not UNSET:
            field_dict["disclose"] = disclose
        if discovery_exchange_id is not UNSET:
            field_dict["discovery_exchange_id"] = discovery_exchange_id
        if query_msg is not UNSET:
            field_dict["query_msg"] = query_msg
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

        _disclose = d.pop("disclose", UNSET)
        disclose: Union[Unset, Disclose]
        if isinstance(_disclose, Unset):
            disclose = UNSET
        else:
            disclose = Disclose.from_dict(_disclose)

        discovery_exchange_id = d.pop("discovery_exchange_id", UNSET)

        _query_msg = d.pop("query_msg", UNSET)
        query_msg: Union[Unset, Query]
        if isinstance(_query_msg, Unset):
            query_msg = UNSET
        else:
            query_msg = Query.from_dict(_query_msg)

        state = d.pop("state", UNSET)

        thread_id = d.pop("thread_id", UNSET)

        trace = d.pop("trace", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        v10_discovery_record = cls(
            connection_id=connection_id,
            created_at=created_at,
            disclose=disclose,
            discovery_exchange_id=discovery_exchange_id,
            query_msg=query_msg,
            state=state,
            thread_id=thread_id,
            trace=trace,
            updated_at=updated_at,
        )

        v10_discovery_record.additional_properties = d
        return v10_discovery_record

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
