from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.claim_format_jwt import ClaimFormatJwt
from ..models.claim_format_jwt_vc import ClaimFormatJwtVc
from ..models.claim_format_jwt_vp import ClaimFormatJwtVp
from ..models.claim_format_ldp import ClaimFormatLdp
from ..models.claim_format_ldp_vc import ClaimFormatLdpVc
from ..models.claim_format_ldp_vp import ClaimFormatLdpVp
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClaimFormat")


@attr.s(auto_attribs=True)
class ClaimFormat:
    """
    Attributes:
        jwt (Union[Unset, ClaimFormatJwt]):
        jwt_vc (Union[Unset, ClaimFormatJwtVc]):
        jwt_vp (Union[Unset, ClaimFormatJwtVp]):
        ldp (Union[Unset, ClaimFormatLdp]):
        ldp_vc (Union[Unset, ClaimFormatLdpVc]):
        ldp_vp (Union[Unset, ClaimFormatLdpVp]):
    """

    jwt: Union[Unset, ClaimFormatJwt] = UNSET
    jwt_vc: Union[Unset, ClaimFormatJwtVc] = UNSET
    jwt_vp: Union[Unset, ClaimFormatJwtVp] = UNSET
    ldp: Union[Unset, ClaimFormatLdp] = UNSET
    ldp_vc: Union[Unset, ClaimFormatLdpVc] = UNSET
    ldp_vp: Union[Unset, ClaimFormatLdpVp] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        jwt: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.jwt, Unset):
            jwt = self.jwt.to_dict()

        jwt_vc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.jwt_vc, Unset):
            jwt_vc = self.jwt_vc.to_dict()

        jwt_vp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.jwt_vp, Unset):
            jwt_vp = self.jwt_vp.to_dict()

        ldp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ldp, Unset):
            ldp = self.ldp.to_dict()

        ldp_vc: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ldp_vc, Unset):
            ldp_vc = self.ldp_vc.to_dict()

        ldp_vp: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ldp_vp, Unset):
            ldp_vp = self.ldp_vp.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if jwt is not UNSET:
            field_dict["jwt"] = jwt
        if jwt_vc is not UNSET:
            field_dict["jwt_vc"] = jwt_vc
        if jwt_vp is not UNSET:
            field_dict["jwt_vp"] = jwt_vp
        if ldp is not UNSET:
            field_dict["ldp"] = ldp
        if ldp_vc is not UNSET:
            field_dict["ldp_vc"] = ldp_vc
        if ldp_vp is not UNSET:
            field_dict["ldp_vp"] = ldp_vp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _jwt = d.pop("jwt", UNSET)
        jwt: Union[Unset, ClaimFormatJwt]
        if isinstance(_jwt, Unset):
            jwt = UNSET
        else:
            jwt = ClaimFormatJwt.from_dict(_jwt)

        _jwt_vc = d.pop("jwt_vc", UNSET)
        jwt_vc: Union[Unset, ClaimFormatJwtVc]
        if isinstance(_jwt_vc, Unset):
            jwt_vc = UNSET
        else:
            jwt_vc = ClaimFormatJwtVc.from_dict(_jwt_vc)

        _jwt_vp = d.pop("jwt_vp", UNSET)
        jwt_vp: Union[Unset, ClaimFormatJwtVp]
        if isinstance(_jwt_vp, Unset):
            jwt_vp = UNSET
        else:
            jwt_vp = ClaimFormatJwtVp.from_dict(_jwt_vp)

        _ldp = d.pop("ldp", UNSET)
        ldp: Union[Unset, ClaimFormatLdp]
        if isinstance(_ldp, Unset):
            ldp = UNSET
        else:
            ldp = ClaimFormatLdp.from_dict(_ldp)

        _ldp_vc = d.pop("ldp_vc", UNSET)
        ldp_vc: Union[Unset, ClaimFormatLdpVc]
        if isinstance(_ldp_vc, Unset):
            ldp_vc = UNSET
        else:
            ldp_vc = ClaimFormatLdpVc.from_dict(_ldp_vc)

        _ldp_vp = d.pop("ldp_vp", UNSET)
        ldp_vp: Union[Unset, ClaimFormatLdpVp]
        if isinstance(_ldp_vp, Unset):
            ldp_vp = UNSET
        else:
            ldp_vp = ClaimFormatLdpVp.from_dict(_ldp_vp)

        claim_format = cls(
            jwt=jwt,
            jwt_vc=jwt_vc,
            jwt_vp=jwt_vp,
            ldp=ldp,
            ldp_vc=ldp_vc,
            ldp_vp=ldp_vp,
        )

        claim_format.additional_properties = d
        return claim_format

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
