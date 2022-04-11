from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EndorserInfo")


@attr.s(auto_attribs=True)
class EndorserInfo:
    """
    Attributes:
        endorser_did (str): Endorser DID
        endorser_name (Union[Unset, str]): Endorser Name
    """

    endorser_did: str
    endorser_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        endorser_did = self.endorser_did
        endorser_name = self.endorser_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "endorser_did": endorser_did,
            }
        )
        if endorser_name is not UNSET:
            field_dict["endorser_name"] = endorser_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        endorser_did = d.pop("endorser_did")

        endorser_name = d.pop("endorser_name", UNSET)

        endorser_info = cls(
            endorser_did=endorser_did,
            endorser_name=endorser_name,
        )

        endorser_info.additional_properties = d
        return endorser_info

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
