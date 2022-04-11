from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyRequestedCredsRequestedAttr")


@attr.s(auto_attribs=True)
class IndyRequestedCredsRequestedAttr:
    """
    Attributes:
        cred_id (str): Wallet credential identifier (typically but not necessarily a UUID) Example:
            3fa85f64-5717-4562-b3fc-2c963f66afa6.
        revealed (Union[Unset, bool]): Whether to reveal attribute in proof (default true)
    """

    cred_id: str
    revealed: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cred_id = self.cred_id
        revealed = self.revealed

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cred_id": cred_id,
            }
        )
        if revealed is not UNSET:
            field_dict["revealed"] = revealed

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cred_id = d.pop("cred_id")

        revealed = d.pop("revealed", UNSET)

        indy_requested_creds_requested_attr = cls(
            cred_id=cred_id,
            revealed=revealed,
        )

        indy_requested_creds_requested_attr.additional_properties = d
        return indy_requested_creds_requested_attr

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
