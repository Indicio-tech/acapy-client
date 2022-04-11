from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.transaction_jobs_transaction_my_job import TransactionJobsTransactionMyJob
from ..models.transaction_jobs_transaction_their_job import TransactionJobsTransactionTheirJob
from ..types import UNSET, Unset

T = TypeVar("T", bound="TransactionJobs")


@attr.s(auto_attribs=True)
class TransactionJobs:
    """
    Attributes:
        transaction_my_job (Union[Unset, TransactionJobsTransactionMyJob]): My transaction related job
        transaction_their_job (Union[Unset, TransactionJobsTransactionTheirJob]): Their transaction related job
    """

    transaction_my_job: Union[Unset, TransactionJobsTransactionMyJob] = UNSET
    transaction_their_job: Union[Unset, TransactionJobsTransactionTheirJob] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        transaction_my_job: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_my_job, Unset):
            transaction_my_job = self.transaction_my_job.value

        transaction_their_job: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_their_job, Unset):
            transaction_their_job = self.transaction_their_job.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if transaction_my_job is not UNSET:
            field_dict["transaction_my_job"] = transaction_my_job
        if transaction_their_job is not UNSET:
            field_dict["transaction_their_job"] = transaction_their_job

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _transaction_my_job = d.pop("transaction_my_job", UNSET)
        transaction_my_job: Union[Unset, TransactionJobsTransactionMyJob]
        if isinstance(_transaction_my_job, Unset):
            transaction_my_job = UNSET
        else:
            transaction_my_job = TransactionJobsTransactionMyJob(_transaction_my_job)

        _transaction_their_job = d.pop("transaction_their_job", UNSET)
        transaction_their_job: Union[Unset, TransactionJobsTransactionTheirJob]
        if isinstance(_transaction_their_job, Unset):
            transaction_their_job = UNSET
        else:
            transaction_their_job = TransactionJobsTransactionTheirJob(_transaction_their_job)

        transaction_jobs = cls(
            transaction_my_job=transaction_my_job,
            transaction_their_job=transaction_their_job,
        )

        transaction_jobs.additional_properties = d
        return transaction_jobs

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
