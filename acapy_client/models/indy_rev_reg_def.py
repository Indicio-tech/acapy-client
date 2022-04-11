from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_rev_reg_def_revoc_def_type import IndyRevRegDefRevocDefType
from ..models.indy_rev_reg_def_value import IndyRevRegDefValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyRevRegDef")


@attr.s(auto_attribs=True)
class IndyRevRegDef:
    """
    Attributes:
        cred_def_id (Union[Unset, str]): Credential definition identifier Example: WgWxqztrNooG92RXvxSTWv:3:CL:20:tag.
        id (Union[Unset, str]): Indy revocation registry identifier Example:
            WgWxqztrNooG92RXvxSTWv:4:WgWxqztrNooG92RXvxSTWv:3:CL:20:tag:CL_ACCUM:0.
        revoc_def_type (Union[Unset, IndyRevRegDefRevocDefType]): Revocation registry type (specify CL_ACCUM) Example:
            CL_ACCUM.
        tag (Union[Unset, str]): Revocation registry tag
        value (Union[Unset, IndyRevRegDefValue]):
        ver (Union[Unset, str]): Version of revocation registry definition Example: 1.0.
    """

    cred_def_id: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    revoc_def_type: Union[Unset, IndyRevRegDefRevocDefType] = UNSET
    tag: Union[Unset, str] = UNSET
    value: Union[Unset, IndyRevRegDefValue] = UNSET
    ver: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cred_def_id = self.cred_def_id
        id = self.id
        revoc_def_type: Union[Unset, str] = UNSET
        if not isinstance(self.revoc_def_type, Unset):
            revoc_def_type = self.revoc_def_type.value

        tag = self.tag
        value: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value.to_dict()

        ver = self.ver

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cred_def_id is not UNSET:
            field_dict["credDefId"] = cred_def_id
        if id is not UNSET:
            field_dict["id"] = id
        if revoc_def_type is not UNSET:
            field_dict["revocDefType"] = revoc_def_type
        if tag is not UNSET:
            field_dict["tag"] = tag
        if value is not UNSET:
            field_dict["value"] = value
        if ver is not UNSET:
            field_dict["ver"] = ver

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        cred_def_id = d.pop("credDefId", UNSET)

        id = d.pop("id", UNSET)

        _revoc_def_type = d.pop("revocDefType", UNSET)
        revoc_def_type: Union[Unset, IndyRevRegDefRevocDefType]
        if isinstance(_revoc_def_type, Unset):
            revoc_def_type = UNSET
        else:
            revoc_def_type = IndyRevRegDefRevocDefType(_revoc_def_type)

        tag = d.pop("tag", UNSET)

        _value = d.pop("value", UNSET)
        value: Union[Unset, IndyRevRegDefValue]
        if isinstance(_value, Unset):
            value = UNSET
        else:
            value = IndyRevRegDefValue.from_dict(_value)

        ver = d.pop("ver", UNSET)

        indy_rev_reg_def = cls(
            cred_def_id=cred_def_id,
            id=id,
            revoc_def_type=revoc_def_type,
            tag=tag,
            value=value,
            ver=ver,
        )

        indy_rev_reg_def.additional_properties = d
        return indy_rev_reg_def

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
