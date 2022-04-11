from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.aml_record import AMLRecord
from ..models.taa_acceptance import TAAAcceptance
from ..models.taa_record import TAARecord
from ..types import UNSET, Unset

T = TypeVar("T", bound="TAAInfo")


@attr.s(auto_attribs=True)
class TAAInfo:
    """
    Attributes:
        aml_record (Union[Unset, AMLRecord]):
        taa_accepted (Union[Unset, None, TAAAcceptance]):
        taa_record (Union[Unset, TAARecord]):
        taa_required (Union[Unset, bool]):
    """

    aml_record: Union[Unset, AMLRecord] = UNSET
    taa_accepted: Union[Unset, None, TAAAcceptance] = UNSET
    taa_record: Union[Unset, TAARecord] = UNSET
    taa_required: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aml_record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aml_record, Unset):
            aml_record = self.aml_record.to_dict()

        taa_accepted: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.taa_accepted, Unset):
            taa_accepted = self.taa_accepted.to_dict() if self.taa_accepted else None

        taa_record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.taa_record, Unset):
            taa_record = self.taa_record.to_dict()

        taa_required = self.taa_required

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aml_record is not UNSET:
            field_dict["aml_record"] = aml_record
        if taa_accepted is not UNSET:
            field_dict["taa_accepted"] = taa_accepted
        if taa_record is not UNSET:
            field_dict["taa_record"] = taa_record
        if taa_required is not UNSET:
            field_dict["taa_required"] = taa_required

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _aml_record = d.pop("aml_record", UNSET)
        aml_record: Union[Unset, AMLRecord]
        if isinstance(_aml_record, Unset):
            aml_record = UNSET
        else:
            aml_record = AMLRecord.from_dict(_aml_record)

        _taa_accepted = d.pop("taa_accepted", UNSET)
        taa_accepted: Union[Unset, None, TAAAcceptance]
        if _taa_accepted is None:
            taa_accepted = None
        elif isinstance(_taa_accepted, Unset):
            taa_accepted = UNSET
        else:
            taa_accepted = TAAAcceptance.from_dict(_taa_accepted)

        _taa_record = d.pop("taa_record", UNSET)
        taa_record: Union[Unset, TAARecord]
        if isinstance(_taa_record, Unset):
            taa_record = UNSET
        else:
            taa_record = TAARecord.from_dict(_taa_record)

        taa_required = d.pop("taa_required", UNSET)

        taa_info = cls(
            aml_record=aml_record,
            taa_accepted=taa_accepted,
            taa_record=taa_record,
            taa_required=taa_required,
        )

        taa_info.additional_properties = d
        return taa_info

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
