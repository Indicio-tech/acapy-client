from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.create_wallet_response_key_management_mode import CreateWalletResponseKeyManagementMode
from ..models.create_wallet_response_settings import CreateWalletResponseSettings
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWalletResponse")


@attr.s(auto_attribs=True)
class CreateWalletResponse:
    """
    Attributes:
        key_management_mode (CreateWalletResponseKeyManagementMode): Mode regarding management of wallet key
        wallet_id (str): Wallet record ID Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        created_at (Union[Unset, str]): Time of record creation Example: 2021-12-31 23:59:59+00:00.
        settings (Union[Unset, CreateWalletResponseSettings]): Settings for this wallet.
        state (Union[Unset, str]): Current record state Example: active.
        token (Union[Unset, str]): Authorization token to authenticate wallet requests Example:
            eyJhbGciOiJFZERTQSJ9.eyJhIjogIjAifQ.dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk.
        updated_at (Union[Unset, str]): Time of last record update Example: 2021-12-31 23:59:59+00:00.
    """

    key_management_mode: CreateWalletResponseKeyManagementMode
    wallet_id: str
    created_at: Union[Unset, str] = UNSET
    settings: Union[Unset, CreateWalletResponseSettings] = UNSET
    state: Union[Unset, str] = UNSET
    token: Union[Unset, str] = UNSET
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
        token = self.token
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
        if token is not UNSET:
            field_dict["token"] = token
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key_management_mode = CreateWalletResponseKeyManagementMode(d.pop("key_management_mode"))

        wallet_id = d.pop("wallet_id")

        created_at = d.pop("created_at", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, CreateWalletResponseSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = CreateWalletResponseSettings.from_dict(_settings)

        state = d.pop("state", UNSET)

        token = d.pop("token", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        create_wallet_response = cls(
            key_management_mode=key_management_mode,
            wallet_id=wallet_id,
            created_at=created_at,
            settings=settings,
            state=state,
            token=token,
            updated_at=updated_at,
        )

        create_wallet_response.additional_properties = d
        return create_wallet_response

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
