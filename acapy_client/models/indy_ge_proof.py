from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.indy_ge_proof_pred import IndyGEProofPred
from ..models.indy_ge_proof_r import IndyGEProofR
from ..models.indy_ge_proof_t import IndyGEProofT
from ..models.indy_ge_proof_u import IndyGEProofU
from ..types import UNSET, Unset

T = TypeVar("T", bound="IndyGEProof")


@attr.s(auto_attribs=True)
class IndyGEProof:
    """
    Attributes:
        alpha (Union[Unset, str]):  Example: 0.
        mj (Union[Unset, str]):  Example: 0.
        predicate (Union[Unset, IndyGEProofPred]):
        r (Union[Unset, IndyGEProofR]):
        t (Union[Unset, IndyGEProofT]):
        u (Union[Unset, IndyGEProofU]):
    """

    alpha: Union[Unset, str] = UNSET
    mj: Union[Unset, str] = UNSET
    predicate: Union[Unset, IndyGEProofPred] = UNSET
    r: Union[Unset, IndyGEProofR] = UNSET
    t: Union[Unset, IndyGEProofT] = UNSET
    u: Union[Unset, IndyGEProofU] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alpha = self.alpha
        mj = self.mj
        predicate: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.predicate, Unset):
            predicate = self.predicate.to_dict()

        r: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.r, Unset):
            r = self.r.to_dict()

        t: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.t, Unset):
            t = self.t.to_dict()

        u: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.u, Unset):
            u = self.u.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alpha is not UNSET:
            field_dict["alpha"] = alpha
        if mj is not UNSET:
            field_dict["mj"] = mj
        if predicate is not UNSET:
            field_dict["predicate"] = predicate
        if r is not UNSET:
            field_dict["r"] = r
        if t is not UNSET:
            field_dict["t"] = t
        if u is not UNSET:
            field_dict["u"] = u

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        alpha = d.pop("alpha", UNSET)

        mj = d.pop("mj", UNSET)

        _predicate = d.pop("predicate", UNSET)
        predicate: Union[Unset, IndyGEProofPred]
        if isinstance(_predicate, Unset):
            predicate = UNSET
        else:
            predicate = IndyGEProofPred.from_dict(_predicate)

        _r = d.pop("r", UNSET)
        r: Union[Unset, IndyGEProofR]
        if isinstance(_r, Unset):
            r = UNSET
        else:
            r = IndyGEProofR.from_dict(_r)

        _t = d.pop("t", UNSET)
        t: Union[Unset, IndyGEProofT]
        if isinstance(_t, Unset):
            t = UNSET
        else:
            t = IndyGEProofT.from_dict(_t)

        _u = d.pop("u", UNSET)
        u: Union[Unset, IndyGEProofU]
        if isinstance(_u, Unset):
            u = UNSET
        else:
            u = IndyGEProofU.from_dict(_u)

        indy_ge_proof = cls(
            alpha=alpha,
            mj=mj,
            predicate=predicate,
            r=r,
            t=t,
            u=u,
        )

        indy_ge_proof.additional_properties = d
        return indy_ge_proof

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
