from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.did_key_type import DIDKeyType
from ..models.did_method import DIDMethod
from ..models.did_posture import DIDPosture
from ..types import UNSET, Unset

T = TypeVar("T", bound="DID")


@attr.s(auto_attribs=True)
class DID:
    """
    Attributes:
        did (Union[Unset, str]): DID of interest Example: WgWxqztrNooG92RXvxSTWv.
        key_type (Union[Unset, DIDKeyType]): Key type associated with the DID Example: ed25519.
        method (Union[Unset, DIDMethod]): Did method associated with the DID Example: sov.
        posture (Union[Unset, DIDPosture]): Whether DID is current public DID, posted to ledger but not current public
            DID, or local to the wallet Example: wallet_only.
        verkey (Union[Unset, str]): Public verification key Example: H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV.
    """

    did: Union[Unset, str] = UNSET
    key_type: Union[Unset, DIDKeyType] = UNSET
    method: Union[Unset, DIDMethod] = UNSET
    posture: Union[Unset, DIDPosture] = UNSET
    verkey: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        did = self.did
        key_type: Union[Unset, str] = UNSET
        if not isinstance(self.key_type, Unset):
            key_type = self.key_type.value

        method: Union[Unset, str] = UNSET
        if not isinstance(self.method, Unset):
            method = self.method.value

        posture: Union[Unset, str] = UNSET
        if not isinstance(self.posture, Unset):
            posture = self.posture.value

        verkey = self.verkey

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if did is not UNSET:
            field_dict["did"] = did
        if key_type is not UNSET:
            field_dict["key_type"] = key_type
        if method is not UNSET:
            field_dict["method"] = method
        if posture is not UNSET:
            field_dict["posture"] = posture
        if verkey is not UNSET:
            field_dict["verkey"] = verkey

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        did = d.pop("did", UNSET)

        _key_type = d.pop("key_type", UNSET)
        key_type: Union[Unset, DIDKeyType]
        if isinstance(_key_type, Unset):
            key_type = UNSET
        else:
            key_type = DIDKeyType(_key_type)

        _method = d.pop("method", UNSET)
        method: Union[Unset, DIDMethod]
        if isinstance(_method, Unset):
            method = UNSET
        else:
            method = DIDMethod(_method)

        _posture = d.pop("posture", UNSET)
        posture: Union[Unset, DIDPosture]
        if isinstance(_posture, Unset):
            posture = UNSET
        else:
            posture = DIDPosture(_posture)

        verkey = d.pop("verkey", UNSET)

        did = cls(
            did=did,
            key_type=key_type,
            method=method,
            posture=posture,
            verkey=verkey,
        )

        did.additional_properties = d
        return did

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
