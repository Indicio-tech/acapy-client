from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.generated import Generated
from ..types import UNSET, Unset

T = TypeVar("T", bound="CredDefValuePrimary")


@attr.s(auto_attribs=True)
class CredDefValuePrimary:
    """
    Attributes:
        n (Union[Unset, str]):  Example: 0.
        r (Union[Unset, Generated]):
        rctxt (Union[Unset, str]):  Example: 0.
        s (Union[Unset, str]):  Example: 0.
        z (Union[Unset, str]):  Example: 0.
    """

    n: Union[Unset, str] = UNSET
    r: Union[Unset, Generated] = UNSET
    rctxt: Union[Unset, str] = UNSET
    s: Union[Unset, str] = UNSET
    z: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        n = self.n
        r: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.r, Unset):
            r = self.r.to_dict()

        rctxt = self.rctxt
        s = self.s
        z = self.z

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if n is not UNSET:
            field_dict["n"] = n
        if r is not UNSET:
            field_dict["r"] = r
        if rctxt is not UNSET:
            field_dict["rctxt"] = rctxt
        if s is not UNSET:
            field_dict["s"] = s
        if z is not UNSET:
            field_dict["z"] = z

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        n = d.pop("n", UNSET)

        _r = d.pop("r", UNSET)
        r: Union[Unset, Generated]
        if isinstance(_r, Unset):
            r = UNSET
        else:
            r = Generated.from_dict(_r)

        rctxt = d.pop("rctxt", UNSET)

        s = d.pop("s", UNSET)

        z = d.pop("z", UNSET)

        cred_def_value_primary = cls(
            n=n,
            r=r,
            rctxt=rctxt,
            s=s,
            z=z,
        )

        cred_def_value_primary.additional_properties = d
        return cred_def_value_primary

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
