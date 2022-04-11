from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attach_decorator import AttachDecorator
from ..types import UNSET, Unset

T = TypeVar("T", bound="DIDXRequest")


@attr.s(auto_attribs=True)
class DIDXRequest:
    """
    Attributes:
        label (str): Label for DID exchange request Example: Request to connect with Bob.
        id (Union[Unset, str]): Message identifier Example: 3fa85f64-5717-4562-b3fc-2c963f66afa6.
        type (Union[Unset, str]): Message type Example: https://didcomm.org/my-family/1.0/my-message-type.
        did (Union[Unset, str]): DID of exchange Example: WgWxqztrNooG92RXvxSTWv.
        did_docattach (Union[Unset, AttachDecorator]):
    """

    label: str
    id: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    did: Union[Unset, str] = UNSET
    did_docattach: Union[Unset, AttachDecorator] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        label = self.label
        id = self.id
        type = self.type
        did = self.did
        did_docattach: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.did_docattach, Unset):
            did_docattach = self.did_docattach.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "label": label,
            }
        )
        if id is not UNSET:
            field_dict["@id"] = id
        if type is not UNSET:
            field_dict["@type"] = type
        if did is not UNSET:
            field_dict["did"] = did
        if did_docattach is not UNSET:
            field_dict["did_doc~attach"] = did_docattach

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        label = d.pop("label")

        id = d.pop("@id", UNSET)

        type = d.pop("@type", UNSET)

        did = d.pop("did", UNSET)

        _did_docattach = d.pop("did_doc~attach", UNSET)
        did_docattach: Union[Unset, AttachDecorator]
        if isinstance(_did_docattach, Unset):
            did_docattach = UNSET
        else:
            did_docattach = AttachDecorator.from_dict(_did_docattach)

        didx_request = cls(
            label=label,
            id=id,
            type=type,
            did=did,
            did_docattach=did_docattach,
        )

        didx_request.additional_properties = d
        return didx_request

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
