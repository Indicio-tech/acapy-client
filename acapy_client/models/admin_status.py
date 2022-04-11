from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.admin_status_conductor import AdminStatusConductor
from ..models.admin_status_timing import AdminStatusTiming
from ..types import UNSET, Unset

T = TypeVar("T", bound="AdminStatus")


@attr.s(auto_attribs=True)
class AdminStatus:
    """
    Attributes:
        conductor (Union[Unset, AdminStatusConductor]): Conductor statistics
        label (Union[Unset, None, str]): Default label
        timing (Union[Unset, AdminStatusTiming]): Timing results
        version (Union[Unset, str]): Version code
    """

    conductor: Union[Unset, AdminStatusConductor] = UNSET
    label: Union[Unset, None, str] = UNSET
    timing: Union[Unset, AdminStatusTiming] = UNSET
    version: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        conductor: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conductor, Unset):
            conductor = self.conductor.to_dict()

        label = self.label
        timing: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.timing, Unset):
            timing = self.timing.to_dict()

        version = self.version

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conductor is not UNSET:
            field_dict["conductor"] = conductor
        if label is not UNSET:
            field_dict["label"] = label
        if timing is not UNSET:
            field_dict["timing"] = timing
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _conductor = d.pop("conductor", UNSET)
        conductor: Union[Unset, AdminStatusConductor]
        if isinstance(_conductor, Unset):
            conductor = UNSET
        else:
            conductor = AdminStatusConductor.from_dict(_conductor)

        label = d.pop("label", UNSET)

        _timing = d.pop("timing", UNSET)
        timing: Union[Unset, AdminStatusTiming]
        if isinstance(_timing, Unset):
            timing = UNSET
        else:
            timing = AdminStatusTiming.from_dict(_timing)

        version = d.pop("version", UNSET)

        admin_status = cls(
            conductor=conductor,
            label=label,
            timing=timing,
            version=version,
        )

        admin_status.additional_properties = d
        return admin_status

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
