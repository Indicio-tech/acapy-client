from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.v20_cred_filter import V20CredFilter
from ..models.v20_cred_preview import V20CredPreview
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20CredBoundOfferRequest")


@attr.s(auto_attribs=True)
class V20CredBoundOfferRequest:
    """
    Attributes:
        counter_preview (Union[Unset, V20CredPreview]):
        filter_ (Union[Unset, V20CredFilter]):
    """

    counter_preview: Union[Unset, V20CredPreview] = UNSET
    filter_: Union[Unset, V20CredFilter] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        counter_preview: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.counter_preview, Unset):
            counter_preview = self.counter_preview.to_dict()

        filter_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if counter_preview is not UNSET:
            field_dict["counter_preview"] = counter_preview
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _counter_preview = d.pop("counter_preview", UNSET)
        counter_preview: Union[Unset, V20CredPreview]
        if isinstance(_counter_preview, Unset):
            counter_preview = UNSET
        else:
            counter_preview = V20CredPreview.from_dict(_counter_preview)

        _filter_ = d.pop("filter", UNSET)
        filter_: Union[Unset, V20CredFilter]
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = V20CredFilter.from_dict(_filter_)

        v20_cred_bound_offer_request = cls(
            counter_preview=counter_preview,
            filter_=filter_,
        )

        v20_cred_bound_offer_request.additional_properties = d
        return v20_cred_bound_offer_request

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
