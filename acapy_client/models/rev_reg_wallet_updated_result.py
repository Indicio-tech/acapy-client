from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rev_reg_wallet_updated_result_accum_calculated import RevRegWalletUpdatedResultAccumCalculated
from ..models.rev_reg_wallet_updated_result_accum_fixed import RevRegWalletUpdatedResultAccumFixed
from ..models.rev_reg_wallet_updated_result_rev_reg_delta import RevRegWalletUpdatedResultRevRegDelta
from ..types import UNSET, Unset

T = TypeVar("T", bound="RevRegWalletUpdatedResult")


@attr.s(auto_attribs=True)
class RevRegWalletUpdatedResult:
    """
    Attributes:
        accum_calculated (Union[Unset, RevRegWalletUpdatedResultAccumCalculated]): Calculated accumulator for phantom
            revocations
        accum_fixed (Union[Unset, RevRegWalletUpdatedResultAccumFixed]): Applied ledger transaction to fix revocations
        rev_reg_delta (Union[Unset, RevRegWalletUpdatedResultRevRegDelta]): Indy revocation registry delta
    """

    accum_calculated: Union[Unset, RevRegWalletUpdatedResultAccumCalculated] = UNSET
    accum_fixed: Union[Unset, RevRegWalletUpdatedResultAccumFixed] = UNSET
    rev_reg_delta: Union[Unset, RevRegWalletUpdatedResultRevRegDelta] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        accum_calculated: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accum_calculated, Unset):
            accum_calculated = self.accum_calculated.to_dict()

        accum_fixed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.accum_fixed, Unset):
            accum_fixed = self.accum_fixed.to_dict()

        rev_reg_delta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.rev_reg_delta, Unset):
            rev_reg_delta = self.rev_reg_delta.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accum_calculated is not UNSET:
            field_dict["accum_calculated"] = accum_calculated
        if accum_fixed is not UNSET:
            field_dict["accum_fixed"] = accum_fixed
        if rev_reg_delta is not UNSET:
            field_dict["rev_reg_delta"] = rev_reg_delta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _accum_calculated = d.pop("accum_calculated", UNSET)
        accum_calculated: Union[Unset, RevRegWalletUpdatedResultAccumCalculated]
        if isinstance(_accum_calculated, Unset):
            accum_calculated = UNSET
        else:
            accum_calculated = RevRegWalletUpdatedResultAccumCalculated.from_dict(_accum_calculated)

        _accum_fixed = d.pop("accum_fixed", UNSET)
        accum_fixed: Union[Unset, RevRegWalletUpdatedResultAccumFixed]
        if isinstance(_accum_fixed, Unset):
            accum_fixed = UNSET
        else:
            accum_fixed = RevRegWalletUpdatedResultAccumFixed.from_dict(_accum_fixed)

        _rev_reg_delta = d.pop("rev_reg_delta", UNSET)
        rev_reg_delta: Union[Unset, RevRegWalletUpdatedResultRevRegDelta]
        if isinstance(_rev_reg_delta, Unset):
            rev_reg_delta = UNSET
        else:
            rev_reg_delta = RevRegWalletUpdatedResultRevRegDelta.from_dict(_rev_reg_delta)

        rev_reg_wallet_updated_result = cls(
            accum_calculated=accum_calculated,
            accum_fixed=accum_fixed,
            rev_reg_delta=rev_reg_delta,
        )

        rev_reg_wallet_updated_result.additional_properties = d
        return rev_reg_wallet_updated_result

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
