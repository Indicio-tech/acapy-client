from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CredDefValueRevocation")


@attr.s(auto_attribs=True)
class CredDefValueRevocation:
    """ """

    g: Union[Unset, str] = UNSET
    g_dash: Union[Unset, str] = UNSET
    h: Union[Unset, str] = UNSET
    h0: Union[Unset, str] = UNSET
    h1: Union[Unset, str] = UNSET
    h2: Union[Unset, str] = UNSET
    h_cap: Union[Unset, str] = UNSET
    htilde: Union[Unset, str] = UNSET
    pk: Union[Unset, str] = UNSET
    u: Union[Unset, str] = UNSET
    y: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        g = self.g
        g_dash = self.g_dash
        h = self.h
        h0 = self.h0
        h1 = self.h1
        h2 = self.h2
        h_cap = self.h_cap
        htilde = self.htilde
        pk = self.pk
        u = self.u
        y = self.y

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if g is not UNSET:
            field_dict["g"] = g
        if g_dash is not UNSET:
            field_dict["g_dash"] = g_dash
        if h is not UNSET:
            field_dict["h"] = h
        if h0 is not UNSET:
            field_dict["h0"] = h0
        if h1 is not UNSET:
            field_dict["h1"] = h1
        if h2 is not UNSET:
            field_dict["h2"] = h2
        if h_cap is not UNSET:
            field_dict["h_cap"] = h_cap
        if htilde is not UNSET:
            field_dict["htilde"] = htilde
        if pk is not UNSET:
            field_dict["pk"] = pk
        if u is not UNSET:
            field_dict["u"] = u
        if y is not UNSET:
            field_dict["y"] = y

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        g = d.pop("g", UNSET)

        g_dash = d.pop("g_dash", UNSET)

        h = d.pop("h", UNSET)

        h0 = d.pop("h0", UNSET)

        h1 = d.pop("h1", UNSET)

        h2 = d.pop("h2", UNSET)

        h_cap = d.pop("h_cap", UNSET)

        htilde = d.pop("htilde", UNSET)

        pk = d.pop("pk", UNSET)

        u = d.pop("u", UNSET)

        y = d.pop("y", UNSET)

        cred_def_value_revocation = cls(
            g=g,
            g_dash=g_dash,
            h=h,
            h0=h0,
            h1=h1,
            h2=h2,
            h_cap=h_cap,
            htilde=htilde,
            pk=pk,
            u=u,
            y=y,
        )

        cred_def_value_revocation.additional_properties = d
        return cred_def_value_revocation

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
