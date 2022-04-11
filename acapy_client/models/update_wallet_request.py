from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.update_wallet_request_wallet_dispatch_type import UpdateWalletRequestWalletDispatchType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateWalletRequest")


@attr.s(auto_attribs=True)
class UpdateWalletRequest:
    """
    Attributes:
        image_url (Union[Unset, str]): Image url for this wallet. This image url is publicized            (self-
            attested) to other agents as part of forming a connection. Example: https://aries.ca/images/sample.png.
        label (Union[Unset, str]): Label for this wallet. This label is publicized            (self-attested) to other
            agents as part of forming a connection. Example: Alice.
        wallet_dispatch_type (Union[Unset, UpdateWalletRequestWalletDispatchType]): Webhook target dispatch type for
            this wallet.             default - Dispatch only to webhooks associated with this wallet.             base -
            Dispatch only to webhooks associated with the base wallet.             both - Dispatch to both webhook targets.
            Example: default.
        wallet_webhook_urls (Union[Unset, List[str]]): List of Webhook URLs associated with this subwallet
    """

    image_url: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    wallet_dispatch_type: Union[Unset, UpdateWalletRequestWalletDispatchType] = UNSET
    wallet_webhook_urls: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        image_url = self.image_url
        label = self.label
        wallet_dispatch_type: Union[Unset, str] = UNSET
        if not isinstance(self.wallet_dispatch_type, Unset):
            wallet_dispatch_type = self.wallet_dispatch_type.value

        wallet_webhook_urls: Union[Unset, List[str]] = UNSET
        if not isinstance(self.wallet_webhook_urls, Unset):
            wallet_webhook_urls = self.wallet_webhook_urls

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if label is not UNSET:
            field_dict["label"] = label
        if wallet_dispatch_type is not UNSET:
            field_dict["wallet_dispatch_type"] = wallet_dispatch_type
        if wallet_webhook_urls is not UNSET:
            field_dict["wallet_webhook_urls"] = wallet_webhook_urls

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        image_url = d.pop("image_url", UNSET)

        label = d.pop("label", UNSET)

        _wallet_dispatch_type = d.pop("wallet_dispatch_type", UNSET)
        wallet_dispatch_type: Union[Unset, UpdateWalletRequestWalletDispatchType]
        if isinstance(_wallet_dispatch_type, Unset):
            wallet_dispatch_type = UNSET
        else:
            wallet_dispatch_type = UpdateWalletRequestWalletDispatchType(_wallet_dispatch_type)

        wallet_webhook_urls = cast(List[str], d.pop("wallet_webhook_urls", UNSET))

        update_wallet_request = cls(
            image_url=image_url,
            label=label,
            wallet_dispatch_type=wallet_dispatch_type,
            wallet_webhook_urls=wallet_webhook_urls,
        )

        update_wallet_request.additional_properties = d
        return update_wallet_request

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
