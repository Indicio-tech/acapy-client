from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.dif_pres_spec import DIFPresSpec
from ..models.indy_pres_spec import IndyPresSpec
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20PresSpecByFormatRequest")


@attr.s(auto_attribs=True)
class V20PresSpecByFormatRequest:
    """
    Attributes:
        dif (Union[Unset, DIFPresSpec]):
        indy (Union[Unset, IndyPresSpec]):
        trace (Union[Unset, bool]): Record trace information, based on agent configuration
    """

    dif: Union[Unset, DIFPresSpec] = UNSET
    indy: Union[Unset, IndyPresSpec] = UNSET
    trace: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dif: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dif, Unset):
            dif = self.dif.to_dict()

        indy: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.indy, Unset):
            indy = self.indy.to_dict()

        trace = self.trace

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dif is not UNSET:
            field_dict["dif"] = dif
        if indy is not UNSET:
            field_dict["indy"] = indy
        if trace is not UNSET:
            field_dict["trace"] = trace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _dif = d.pop("dif", UNSET)
        dif: Union[Unset, DIFPresSpec]
        if isinstance(_dif, Unset):
            dif = UNSET
        else:
            dif = DIFPresSpec.from_dict(_dif)

        _indy = d.pop("indy", UNSET)
        indy: Union[Unset, IndyPresSpec]
        if isinstance(_indy, Unset):
            indy = UNSET
        else:
            indy = IndyPresSpec.from_dict(_indy)

        trace = d.pop("trace", UNSET)

        v20_pres_spec_by_format_request = cls(
            dif=dif,
            indy=indy,
            trace=trace,
        )

        v20_pres_spec_by_format_request.additional_properties = d
        return v20_pres_spec_by_format_request

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
