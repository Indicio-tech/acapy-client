from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_rev_reg_def_value_issuance_type import IndyRevRegDefValueIssuanceType
from ..models.indy_rev_reg_def_value_public_keys import IndyRevRegDefValuePublicKeys
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyRevRegDefValue")


@attr.s(auto_attribs=True)
class IndyRevRegDefValue:
    """
    Attributes:
        issuance_type (Union[Unset, IndyRevRegDefValueIssuanceType]): Issuance type
        max_cred_num (Union[Unset, int]): Maximum number of credentials; registry size Example: 10.
        public_keys (Union[Unset, IndyRevRegDefValuePublicKeys]):
        tails_hash (Union[Unset, str]): Tails hash value Example: H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV.
        tails_location (Union[Unset, str]): Tails file location
    """

    issuance_type: Union[Unset, IndyRevRegDefValueIssuanceType] = UNSET
    max_cred_num: Union[Unset, int] = UNSET
    public_keys: Union[Unset, IndyRevRegDefValuePublicKeys] = UNSET
    tails_hash: Union[Unset, str] = UNSET
    tails_location: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issuance_type: Union[Unset, str] = UNSET
        if not isinstance(self.issuance_type, Unset):
            issuance_type = self.issuance_type.value

        max_cred_num = self.max_cred_num
        public_keys: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.public_keys, Unset):
            public_keys = self.public_keys.to_dict()

        tails_hash = self.tails_hash
        tails_location = self.tails_location

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issuance_type is not UNSET:
            field_dict["issuanceType"] = issuance_type
        if max_cred_num is not UNSET:
            field_dict["maxCredNum"] = max_cred_num
        if public_keys is not UNSET:
            field_dict["publicKeys"] = public_keys
        if tails_hash is not UNSET:
            field_dict["tailsHash"] = tails_hash
        if tails_location is not UNSET:
            field_dict["tailsLocation"] = tails_location

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _issuance_type = d.pop("issuanceType", UNSET)
        issuance_type: Union[Unset, IndyRevRegDefValueIssuanceType]
        if isinstance(_issuance_type, Unset):
            issuance_type = UNSET
        else:
            issuance_type = IndyRevRegDefValueIssuanceType(_issuance_type)

        max_cred_num = d.pop("maxCredNum", UNSET)

        _public_keys = d.pop("publicKeys", UNSET)
        public_keys: Union[Unset, IndyRevRegDefValuePublicKeys]
        if isinstance(_public_keys, Unset):
            public_keys = UNSET
        else:
            public_keys = IndyRevRegDefValuePublicKeys.from_dict(_public_keys)

        tails_hash = d.pop("tailsHash", UNSET)

        tails_location = d.pop("tailsLocation", UNSET)

        indy_rev_reg_def_value = cls(
            issuance_type=issuance_type,
            max_cred_num=max_cred_num,
            public_keys=public_keys,
            tails_hash=tails_hash,
            tails_location=tails_location,
        )

        indy_rev_reg_def_value.additional_properties = d
        return indy_rev_reg_def_value

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
