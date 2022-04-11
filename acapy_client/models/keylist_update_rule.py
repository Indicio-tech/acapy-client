from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.keylist_update_rule_action import KeylistUpdateRuleAction

T = TypeVar("T", bound="KeylistUpdateRule")


@attr.s(auto_attribs=True)
class KeylistUpdateRule:
    """
    Attributes:
        action (KeylistUpdateRuleAction): Action for specific key Example: add.
        recipient_key (str): Key to remove or add Example: H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV.
    """

    action: KeylistUpdateRuleAction
    recipient_key: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        action = self.action.value

        recipient_key = self.recipient_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "recipient_key": recipient_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        action = KeylistUpdateRuleAction(d.pop("action"))

        recipient_key = d.pop("recipient_key")

        keylist_update_rule = cls(
            action=action,
            recipient_key=recipient_key,
        )

        keylist_update_rule.additional_properties = d
        return keylist_update_rule

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
