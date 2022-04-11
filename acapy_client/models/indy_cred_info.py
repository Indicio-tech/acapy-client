from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_cred_info_attrs import IndyCredInfoAttrs
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyCredInfo")


@attr.s(auto_attribs=True)
class IndyCredInfo:
    """
    Attributes:
        attrs (Union[Unset, IndyCredInfoAttrs]): Attribute names and value
        cred_def_id (Union[Unset, str]): Credential definition identifier Example: WgWxqztrNooG92RXvxSTWv:3:CL:20:tag.
        cred_rev_id (Union[Unset, None, str]): Credential revocation identifier Example: 12345.
        referent (Union[Unset, str]): Wallet referent Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        rev_reg_id (Union[Unset, None, str]): Revocation registry identifier Example:
            WgWxqztrNooG92RXvxSTWv:4:WgWxqztrNooG92RXvxSTWv:3:CL:20:tag:CL_ACCUM:0.
        schema_id (Union[Unset, str]): Schema identifier Example: WgWxqztrNooG92RXvxSTWv:2:schema_name:1.0.
    """

    attrs: Union[Unset, IndyCredInfoAttrs] = UNSET
    cred_def_id: Union[Unset, str] = UNSET
    cred_rev_id: Union[Unset, None, str] = UNSET
    referent: Union[Unset, str] = UNSET
    rev_reg_id: Union[Unset, None, str] = UNSET
    schema_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attrs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attrs, Unset):
            attrs = self.attrs.to_dict()

        cred_def_id = self.cred_def_id
        cred_rev_id = self.cred_rev_id
        referent = self.referent
        rev_reg_id = self.rev_reg_id
        schema_id = self.schema_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attrs is not UNSET:
            field_dict["attrs"] = attrs
        if cred_def_id is not UNSET:
            field_dict["cred_def_id"] = cred_def_id
        if cred_rev_id is not UNSET:
            field_dict["cred_rev_id"] = cred_rev_id
        if referent is not UNSET:
            field_dict["referent"] = referent
        if rev_reg_id is not UNSET:
            field_dict["rev_reg_id"] = rev_reg_id
        if schema_id is not UNSET:
            field_dict["schema_id"] = schema_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _attrs = d.pop("attrs", UNSET)
        attrs: Union[Unset, IndyCredInfoAttrs]
        if isinstance(_attrs, Unset):
            attrs = UNSET
        else:
            attrs = IndyCredInfoAttrs.from_dict(_attrs)

        cred_def_id = d.pop("cred_def_id", UNSET)

        cred_rev_id = d.pop("cred_rev_id", UNSET)

        referent = d.pop("referent", UNSET)

        rev_reg_id = d.pop("rev_reg_id", UNSET)

        schema_id = d.pop("schema_id", UNSET)

        indy_cred_info = cls(
            attrs=attrs,
            cred_def_id=cred_def_id,
            cred_rev_id=cred_rev_id,
            referent=referent,
            rev_reg_id=rev_reg_id,
            schema_id=schema_id,
        )

        indy_cred_info.additional_properties = d
        return indy_cred_info

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
