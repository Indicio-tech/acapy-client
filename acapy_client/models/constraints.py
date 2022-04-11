from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.constraints_status_active import ConstraintsStatusActive
from ..models.constraints_status_revoked import ConstraintsStatusRevoked
from ..models.constraints_status_suspended import ConstraintsStatusSuspended
from ..models.constraints_subject_is_issuer import ConstraintsSubjectIsIssuer
from ..models.dif_field import DIFField
from ..models.dif_holder import DIFHolder
from ..types import UNSET, Unset

T = TypeVar("T", bound="Constraints")


@attr.s(auto_attribs=True)
class Constraints:
    """
    Attributes:
        fields (Union[Unset, List[DIFField]]):
        is_holder (Union[Unset, List[DIFHolder]]):
        limit_disclosure (Union[Unset, str]): LimitDisclosure
        status_active (Union[Unset, ConstraintsStatusActive]):
        status_revoked (Union[Unset, ConstraintsStatusRevoked]):
        status_suspended (Union[Unset, ConstraintsStatusSuspended]):
        subject_is_issuer (Union[Unset, ConstraintsSubjectIsIssuer]): SubjectIsIssuer
    """

    fields: Union[Unset, List[DIFField]] = UNSET
    is_holder: Union[Unset, List[DIFHolder]] = UNSET
    limit_disclosure: Union[Unset, str] = UNSET
    status_active: Union[Unset, ConstraintsStatusActive] = UNSET
    status_revoked: Union[Unset, ConstraintsStatusRevoked] = UNSET
    status_suspended: Union[Unset, ConstraintsStatusSuspended] = UNSET
    subject_is_issuer: Union[Unset, ConstraintsSubjectIsIssuer] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()

                fields.append(fields_item)

        is_holder: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.is_holder, Unset):
            is_holder = []
            for is_holder_item_data in self.is_holder:
                is_holder_item = is_holder_item_data.to_dict()

                is_holder.append(is_holder_item)

        limit_disclosure = self.limit_disclosure
        status_active: Union[Unset, str] = UNSET
        if not isinstance(self.status_active, Unset):
            status_active = self.status_active.value

        status_revoked: Union[Unset, str] = UNSET
        if not isinstance(self.status_revoked, Unset):
            status_revoked = self.status_revoked.value

        status_suspended: Union[Unset, str] = UNSET
        if not isinstance(self.status_suspended, Unset):
            status_suspended = self.status_suspended.value

        subject_is_issuer: Union[Unset, str] = UNSET
        if not isinstance(self.subject_is_issuer, Unset):
            subject_is_issuer = self.subject_is_issuer.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fields is not UNSET:
            field_dict["fields"] = fields
        if is_holder is not UNSET:
            field_dict["is_holder"] = is_holder
        if limit_disclosure is not UNSET:
            field_dict["limit_disclosure"] = limit_disclosure
        if status_active is not UNSET:
            field_dict["status_active"] = status_active
        if status_revoked is not UNSET:
            field_dict["status_revoked"] = status_revoked
        if status_suspended is not UNSET:
            field_dict["status_suspended"] = status_suspended
        if subject_is_issuer is not UNSET:
            field_dict["subject_is_issuer"] = subject_is_issuer

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = DIFField.from_dict(fields_item_data)

            fields.append(fields_item)

        is_holder = []
        _is_holder = d.pop("is_holder", UNSET)
        for is_holder_item_data in _is_holder or []:
            is_holder_item = DIFHolder.from_dict(is_holder_item_data)

            is_holder.append(is_holder_item)

        limit_disclosure = d.pop("limit_disclosure", UNSET)

        _status_active = d.pop("status_active", UNSET)
        status_active: Union[Unset, ConstraintsStatusActive]
        if isinstance(_status_active, Unset):
            status_active = UNSET
        else:
            status_active = ConstraintsStatusActive(_status_active)

        _status_revoked = d.pop("status_revoked", UNSET)
        status_revoked: Union[Unset, ConstraintsStatusRevoked]
        if isinstance(_status_revoked, Unset):
            status_revoked = UNSET
        else:
            status_revoked = ConstraintsStatusRevoked(_status_revoked)

        _status_suspended = d.pop("status_suspended", UNSET)
        status_suspended: Union[Unset, ConstraintsStatusSuspended]
        if isinstance(_status_suspended, Unset):
            status_suspended = UNSET
        else:
            status_suspended = ConstraintsStatusSuspended(_status_suspended)

        _subject_is_issuer = d.pop("subject_is_issuer", UNSET)
        subject_is_issuer: Union[Unset, ConstraintsSubjectIsIssuer]
        if isinstance(_subject_is_issuer, Unset):
            subject_is_issuer = UNSET
        else:
            subject_is_issuer = ConstraintsSubjectIsIssuer(_subject_is_issuer)

        constraints = cls(
            fields=fields,
            is_holder=is_holder,
            limit_disclosure=limit_disclosure,
            status_active=status_active,
            status_revoked=status_revoked,
            status_suspended=status_suspended,
            subject_is_issuer=subject_is_issuer,
        )

        constraints.additional_properties = d
        return constraints

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
