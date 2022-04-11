from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoveWalletRequest")


@attr.s(auto_attribs=True)
class RemoveWalletRequest:
    """
    Attributes:
        wallet_key (Union[Unset, str]): Master key used for key derivation. Only required for             unmanaged
            wallets. Example: MySecretKey123.
    """

    wallet_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        wallet_key = self.wallet_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if wallet_key is not UNSET:
            field_dict["wallet_key"] = wallet_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        wallet_key = d.pop("wallet_key", UNSET)

        remove_wallet_request = cls(
            wallet_key=wallet_key,
        )

        remove_wallet_request.additional_properties = d
        return remove_wallet_request

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
