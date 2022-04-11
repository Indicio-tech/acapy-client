from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.credential import Credential
from ..models.ld_proof_vc_detail_options import LDProofVCDetailOptions

T = TypeVar("T", bound="LDProofVCDetail")


@attr.s(auto_attribs=True)
class LDProofVCDetail:
    """
    Attributes:
        credential (Credential):
        options (LDProofVCDetailOptions):
    """

    credential: Credential
    options: LDProofVCDetailOptions
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        credential = self.credential.to_dict()

        options = self.options.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "credential": credential,
                "options": options,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        credential = Credential.from_dict(d.pop("credential"))

        options = LDProofVCDetailOptions.from_dict(d.pop("options"))

        ld_proof_vc_detail = cls(
            credential=credential,
            options=options,
        )

        ld_proof_vc_detail.additional_properties = d
        return ld_proof_vc_detail

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
