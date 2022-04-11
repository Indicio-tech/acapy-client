from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.v20_cred_filter import V20CredFilter
from ..models.v20_cred_preview import V20CredPreview
from ..types import UNSET, Unset

T = TypeVar("T", bound="V20IssueCredSchemaCore")


@attr.s(auto_attribs=True)
class V20IssueCredSchemaCore:
    """
    Attributes:
        filter_ (V20CredFilter):
        auto_remove (Union[Unset, bool]): Whether to remove the credential exchange record on completion (overrides
            --preserve-exchange-records configuration setting)
        comment (Union[Unset, None, str]): Human-readable comment
        credential_preview (Union[Unset, V20CredPreview]):
        trace (Union[Unset, bool]): Record trace information, based on agent configuration
    """

    filter_: V20CredFilter
    auto_remove: Union[Unset, bool] = UNSET
    comment: Union[Unset, None, str] = UNSET
    credential_preview: Union[Unset, V20CredPreview] = UNSET
    trace: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        filter_ = self.filter_.to_dict()

        auto_remove = self.auto_remove
        comment = self.comment
        credential_preview: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.credential_preview, Unset):
            credential_preview = self.credential_preview.to_dict()

        trace = self.trace

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter": filter_,
            }
        )
        if auto_remove is not UNSET:
            field_dict["auto_remove"] = auto_remove
        if comment is not UNSET:
            field_dict["comment"] = comment
        if credential_preview is not UNSET:
            field_dict["credential_preview"] = credential_preview
        if trace is not UNSET:
            field_dict["trace"] = trace

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        filter_ = V20CredFilter.from_dict(d.pop("filter"))

        auto_remove = d.pop("auto_remove", UNSET)

        comment = d.pop("comment", UNSET)

        _credential_preview = d.pop("credential_preview", UNSET)
        credential_preview: Union[Unset, V20CredPreview]
        if isinstance(_credential_preview, Unset):
            credential_preview = UNSET
        else:
            credential_preview = V20CredPreview.from_dict(_credential_preview)

        trace = d.pop("trace", UNSET)

        v20_issue_cred_schema_core = cls(
            filter_=filter_,
            auto_remove=auto_remove,
            comment=comment,
            credential_preview=credential_preview,
            trace=trace,
        )

        v20_issue_cred_schema_core.additional_properties = d
        return v20_issue_cred_schema_core

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
