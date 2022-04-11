from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LedgerConfigInstance")


@attr.s(auto_attribs=True)
class LedgerConfigInstance:
    """
    Attributes:
        genesis_file (Union[Unset, str]): genesis_file
        genesis_transactions (Union[Unset, str]): genesis_transactions
        genesis_url (Union[Unset, str]): genesis_url
        id (Union[Unset, str]): ledger_id
        is_production (Union[Unset, bool]): is_production
    """

    genesis_file: Union[Unset, str] = UNSET
    genesis_transactions: Union[Unset, str] = UNSET
    genesis_url: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    is_production: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        genesis_file = self.genesis_file
        genesis_transactions = self.genesis_transactions
        genesis_url = self.genesis_url
        id = self.id
        is_production = self.is_production

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if genesis_file is not UNSET:
            field_dict["genesis_file"] = genesis_file
        if genesis_transactions is not UNSET:
            field_dict["genesis_transactions"] = genesis_transactions
        if genesis_url is not UNSET:
            field_dict["genesis_url"] = genesis_url
        if id is not UNSET:
            field_dict["id"] = id
        if is_production is not UNSET:
            field_dict["is_production"] = is_production

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        genesis_file = d.pop("genesis_file", UNSET)

        genesis_transactions = d.pop("genesis_transactions", UNSET)

        genesis_url = d.pop("genesis_url", UNSET)

        id = d.pop("id", UNSET)

        is_production = d.pop("is_production", UNSET)

        ledger_config_instance = cls(
            genesis_file=genesis_file,
            genesis_transactions=genesis_transactions,
            genesis_url=genesis_url,
            id=id,
            is_production=is_production,
        )

        ledger_config_instance.additional_properties = d
        return ledger_config_instance

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
