from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.create_wallet_request_key_management_mode import CreateWalletRequestKeyManagementMode
from ..models.create_wallet_request_wallet_dispatch_type import CreateWalletRequestWalletDispatchType
from ..models.create_wallet_request_wallet_key_derivation import CreateWalletRequestWalletKeyDerivation
from ..models.create_wallet_request_wallet_type import CreateWalletRequestWalletType
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateWalletRequest")


@attr.s(auto_attribs=True)
class CreateWalletRequest:
    """
    Attributes:
        image_url (Union[Unset, str]): Image url for this wallet. This image url is publicized            (self-
            attested) to other agents as part of forming a connection. Example: https://aries.ca/images/sample.png.
        key_management_mode (Union[Unset, CreateWalletRequestKeyManagementMode]): Key management method to use for this
            wallet. Example: managed.
        label (Union[Unset, str]): Label for this wallet. This label is publicized            (self-attested) to other
            agents as part of forming a connection. Example: Alice.
        wallet_dispatch_type (Union[Unset, CreateWalletRequestWalletDispatchType]): Webhook target dispatch type for
            this wallet.             default - Dispatch only to webhooks associated with this wallet.             base -
            Dispatch only to webhooks associated with the base wallet.             both - Dispatch to both webhook targets.
            Example: default.
        wallet_key (Union[Unset, str]): Master key used for key derivation. Example: MySecretKey123.
        wallet_key_derivation (Union[Unset, CreateWalletRequestWalletKeyDerivation]): Key derivation Example: RAW.
        wallet_name (Union[Unset, str]): Wallet name Example: MyNewWallet.
        wallet_type (Union[Unset, CreateWalletRequestWalletType]): Type of the wallet to create Example: indy.
        wallet_webhook_urls (Union[Unset, List[str]]): List of Webhook URLs associated with this subwallet
    """

    image_url: Union[Unset, str] = UNSET
    key_management_mode: Union[Unset, CreateWalletRequestKeyManagementMode] = UNSET
    label: Union[Unset, str] = UNSET
    wallet_dispatch_type: Union[Unset, CreateWalletRequestWalletDispatchType] = UNSET
    wallet_key: Union[Unset, str] = UNSET
    wallet_key_derivation: Union[Unset, CreateWalletRequestWalletKeyDerivation] = UNSET
    wallet_name: Union[Unset, str] = UNSET
    wallet_type: Union[Unset, CreateWalletRequestWalletType] = UNSET
    wallet_webhook_urls: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image_url = self.image_url
        key_management_mode: Union[Unset, str] = UNSET
        if not isinstance(self.key_management_mode, Unset):
            key_management_mode = self.key_management_mode.value

        label = self.label
        wallet_dispatch_type: Union[Unset, str] = UNSET
        if not isinstance(self.wallet_dispatch_type, Unset):
            wallet_dispatch_type = self.wallet_dispatch_type.value

        wallet_key = self.wallet_key
        wallet_key_derivation: Union[Unset, str] = UNSET
        if not isinstance(self.wallet_key_derivation, Unset):
            wallet_key_derivation = self.wallet_key_derivation.value

        wallet_name = self.wallet_name
        wallet_type: Union[Unset, str] = UNSET
        if not isinstance(self.wallet_type, Unset):
            wallet_type = self.wallet_type.value

        wallet_webhook_urls: Union[Unset, List[str]] = UNSET
        if not isinstance(self.wallet_webhook_urls, Unset):
            wallet_webhook_urls = self.wallet_webhook_urls

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if key_management_mode is not UNSET:
            field_dict["key_management_mode"] = key_management_mode
        if label is not UNSET:
            field_dict["label"] = label
        if wallet_dispatch_type is not UNSET:
            field_dict["wallet_dispatch_type"] = wallet_dispatch_type
        if wallet_key is not UNSET:
            field_dict["wallet_key"] = wallet_key
        if wallet_key_derivation is not UNSET:
            field_dict["wallet_key_derivation"] = wallet_key_derivation
        if wallet_name is not UNSET:
            field_dict["wallet_name"] = wallet_name
        if wallet_type is not UNSET:
            field_dict["wallet_type"] = wallet_type
        if wallet_webhook_urls is not UNSET:
            field_dict["wallet_webhook_urls"] = wallet_webhook_urls

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        image_url = d.pop("image_url", UNSET)

        _key_management_mode = d.pop("key_management_mode", UNSET)
        key_management_mode: Union[Unset, CreateWalletRequestKeyManagementMode]
        if isinstance(_key_management_mode, Unset):
            key_management_mode = UNSET
        else:
            key_management_mode = CreateWalletRequestKeyManagementMode(_key_management_mode)

        label = d.pop("label", UNSET)

        _wallet_dispatch_type = d.pop("wallet_dispatch_type", UNSET)
        wallet_dispatch_type: Union[Unset, CreateWalletRequestWalletDispatchType]
        if isinstance(_wallet_dispatch_type, Unset):
            wallet_dispatch_type = UNSET
        else:
            wallet_dispatch_type = CreateWalletRequestWalletDispatchType(_wallet_dispatch_type)

        wallet_key = d.pop("wallet_key", UNSET)

        _wallet_key_derivation = d.pop("wallet_key_derivation", UNSET)
        wallet_key_derivation: Union[Unset, CreateWalletRequestWalletKeyDerivation]
        if isinstance(_wallet_key_derivation, Unset):
            wallet_key_derivation = UNSET
        else:
            wallet_key_derivation = CreateWalletRequestWalletKeyDerivation(_wallet_key_derivation)

        wallet_name = d.pop("wallet_name", UNSET)

        _wallet_type = d.pop("wallet_type", UNSET)
        wallet_type: Union[Unset, CreateWalletRequestWalletType]
        if isinstance(_wallet_type, Unset):
            wallet_type = UNSET
        else:
            wallet_type = CreateWalletRequestWalletType(_wallet_type)

        wallet_webhook_urls = cast(List[str], d.pop("wallet_webhook_urls", UNSET))

        create_wallet_request = cls(
            image_url=image_url,
            key_management_mode=key_management_mode,
            label=label,
            wallet_dispatch_type=wallet_dispatch_type,
            wallet_key=wallet_key,
            wallet_key_derivation=wallet_key_derivation,
            wallet_name=wallet_name,
            wallet_type=wallet_type,
            wallet_webhook_urls=wallet_webhook_urls,
        )

        create_wallet_request.additional_properties = d
        return create_wallet_request

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
