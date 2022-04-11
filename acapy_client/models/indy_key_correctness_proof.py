from typing import Any, Dict, List, Type, TypeVar, cast

import attr

T = TypeVar("T", bound="IndyKeyCorrectnessProof")


@attr.s(auto_attribs=True)
class IndyKeyCorrectnessProof:
    """
    Attributes:
        c (str): c in key correctness proof Example: 0.
        xr_cap (List[List[str]]): xr_cap in key correctness proof
        xz_cap (str): xz_cap in key correctness proof Example: 0.
    """

    c: str
    xr_cap: List[List[str]]
    xz_cap: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        c = self.c
        xr_cap = []
        for xr_cap_item_data in self.xr_cap:
            xr_cap_item = xr_cap_item_data

            xr_cap.append(xr_cap_item)

        xz_cap = self.xz_cap

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "c": c,
                "xr_cap": xr_cap,
                "xz_cap": xz_cap,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        c = d.pop("c")

        xr_cap = []
        _xr_cap = d.pop("xr_cap")
        for xr_cap_item_data in _xr_cap:
            xr_cap_item = cast(List[str], xr_cap_item_data)

            xr_cap.append(xr_cap_item)

        xz_cap = d.pop("xz_cap")

        indy_key_correctness_proof = cls(
            c=c,
            xr_cap=xr_cap,
            xz_cap=xz_cap,
        )

        indy_key_correctness_proof.additional_properties = d
        return indy_key_correctness_proof

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
