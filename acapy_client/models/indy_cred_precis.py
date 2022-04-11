from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.indy_cred_info import IndyCredInfo
from ..models.indy_non_revocation_interval import IndyNonRevocationInterval
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyCredPrecis")


@attr.s(auto_attribs=True)
class IndyCredPrecis:
    """
    Attributes:
        cred_info (Union[Unset, IndyCredInfo]):
        interval (Union[Unset, IndyNonRevocationInterval]):
        presentation_referents (Union[Unset, List[str]]):
    """

    cred_info: Union[Unset, IndyCredInfo] = UNSET
    interval: Union[Unset, IndyNonRevocationInterval] = UNSET
    presentation_referents: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cred_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cred_info, Unset):
            cred_info = self.cred_info.to_dict()

        interval: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.interval, Unset):
            interval = self.interval.to_dict()

        presentation_referents: Union[Unset, List[str]] = UNSET
        if not isinstance(self.presentation_referents, Unset):
            presentation_referents = self.presentation_referents

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cred_info is not UNSET:
            field_dict["cred_info"] = cred_info
        if interval is not UNSET:
            field_dict["interval"] = interval
        if presentation_referents is not UNSET:
            field_dict["presentation_referents"] = presentation_referents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _cred_info = d.pop("cred_info", UNSET)
        cred_info: Union[Unset, IndyCredInfo]
        if isinstance(_cred_info, Unset):
            cred_info = UNSET
        else:
            cred_info = IndyCredInfo.from_dict(_cred_info)

        _interval = d.pop("interval", UNSET)
        interval: Union[Unset, IndyNonRevocationInterval]
        if isinstance(_interval, Unset):
            interval = UNSET
        else:
            interval = IndyNonRevocationInterval.from_dict(_interval)

        presentation_referents = cast(List[str], d.pop("presentation_referents", UNSET))

        indy_cred_precis = cls(
            cred_info=cred_info,
            interval=interval,
            presentation_referents=presentation_referents,
        )

        indy_cred_precis.additional_properties = d
        return indy_cred_precis

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
