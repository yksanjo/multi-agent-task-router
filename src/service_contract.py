from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict


@dataclass(frozen=True)
class ServiceStatus:
    name: str
    healthy: bool
    timestamp: str


def build_status(name: str) -> ServiceStatus:
    return ServiceStatus(
        name=name,
        healthy=True,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


def status_payload(status: ServiceStatus) -> Dict[str, str | bool]:
    return {
        "name": status.name,
        "healthy": status.healthy,
        "timestamp": status.timestamp,
    }
