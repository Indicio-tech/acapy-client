from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="RevRegUpdateTailsFileUri")


@attr.s(auto_attribs=True)
class RevRegUpdateTailsFileUri:
    """
    Attributes:
        tails_public_uri (str): Public URI to the tails file Example: http://192.168.56.133:6543/revocation/registry/WgW
            xqztrNooG92RXvxSTWv:4:WgWxqztrNooG92RXvxSTWv:3:CL:20:tag:CL_ACCUM:0/tails-file.
    """

    tails_public_uri: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        tails_public_uri = self.tails_public_uri

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tails_public_uri": tails_public_uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        tails_public_uri = d.pop("tails_public_uri")

        rev_reg_update_tails_file_uri = cls(
            tails_public_uri=tails_public_uri,
        )

        rev_reg_update_tails_file_uri.additional_properties = d
        return rev_reg_update_tails_file_uri

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
