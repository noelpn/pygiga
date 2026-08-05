# pygiga/safety/policy.py

from dataclasses import dataclass
from enum import Enum


class RiskLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class PolicyDecision:
    allowed: bool
    risk: RiskLevel
    reason: str = ""


class SafetyPolicy:
    def __init__(self):
        self.rules = {
            "read_file": RiskLevel.LOW,
            "write_file": RiskLevel.MEDIUM,
            "delete_file": RiskLevel.HIGH,
            "execute_code": RiskLevel.HIGH,
            "internet_access": RiskLevel.MEDIUM,
            "install_package": RiskLevel.HIGH,
            "system_command": RiskLevel.CRITICAL,
            "access_camera": RiskLevel.CRITICAL,
            "access_microphone": RiskLevel.CRITICAL,
            "send_email": RiskLevel.HIGH,
        }

    def evaluate(self, action: str) -> PolicyDecision:
        risk = self.rules.get(action, RiskLevel.CRITICAL)

        if risk == RiskLevel.CRITICAL:
            return PolicyDecision(
                allowed=False,
                risk=risk,
                reason="Critical-risk action blocked."
            )

        return PolicyDecision(
            allowed=True,
            risk=risk,
            reason="Action allowed."
        )

    def set_risk(self, action: str, risk: RiskLevel):
        self.rules[action] = risk

    def block(self, action: str):
        self.rules[action] = RiskLevel.CRITICAL