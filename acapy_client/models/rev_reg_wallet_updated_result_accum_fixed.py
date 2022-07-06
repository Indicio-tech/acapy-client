from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RevRegWalletUpdatedResultAccumFixed")


@attr.s(auto_attribs=True)
class RevRegWalletUpdatedResultAccumFixed:
    """Applied ledger transaction to fix revocations"""

    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        rev_reg_wallet_updated_result_accum_fixed = cls()

        rev_reg_wallet_updated_result_accum_fixed.additional_properties = d
        return rev_reg_wallet_updated_result_accum_fixed

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
