from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.wallet_record_key_management_mode import WalletRecordKeyManagementMode
from ..models.wallet_record_settings import WalletRecordSettings
from ..types import UNSET, Unset

T = TypeVar("T", bound="WalletRecord")


@attr.s(auto_attribs=True)
class WalletRecord:
    """
    Attributes:
        key_management_mode (WalletRecordKeyManagementMode): Mode regarding management of wallet key
        wallet_id (str): Wallet record ID Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        created_at (Union[Unset, str]): Time of record creation Example: 2021-12-31 23:59:59+00:00.
        settings (Union[Unset, WalletRecordSettings]): Settings for this wallet.
        state (Union[Unset, str]): Current record state Example: active.
        updated_at (Union[Unset, str]): Time of last record update Example: 2021-12-31 23:59:59+00:00.
    """

    key_management_mode: WalletRecordKeyManagementMode
    wallet_id: str
    created_at: Union[Unset, str] = UNSET
    settings: Union[Unset, WalletRecordSettings] = UNSET
    state: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key_management_mode = self.key_management_mode.value

        wallet_id = self.wallet_id
        created_at = self.created_at
        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        state = self.state
        updated_at = self.updated_at

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key_management_mode": key_management_mode,
                "wallet_id": wallet_id,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if settings is not UNSET:
            field_dict["settings"] = settings
        if state is not UNSET:
            field_dict["state"] = state
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_management_mode = WalletRecordKeyManagementMode(d.pop("key_management_mode"))

        wallet_id = d.pop("wallet_id")

        created_at = d.pop("created_at", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, WalletRecordSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = WalletRecordSettings.from_dict(_settings)

        state = d.pop("state", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        wallet_record = cls(
            key_management_mode=key_management_mode,
            wallet_id=wallet_id,
            created_at=created_at,
            settings=settings,
            state=state,
            updated_at=updated_at,
        )

        wallet_record.additional_properties = d
        return wallet_record

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
