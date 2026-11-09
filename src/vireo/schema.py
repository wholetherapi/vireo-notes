"""Rolling schema evolution helpers."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class SchemaVersion:
    version: int
    fields: Dict[str, str] = field(default_factory=dict)

    def is_compatible_with(self, other: "SchemaVersion") -> bool:
        for name, kind in self.fields.items():
            if name in other.fields and other.fields[name] != kind:
                return False
        return True


class SchemaRegistry:
    def __init__(self) -> None:
        self.versions: List[SchemaVersion] = []

    def register(self, version: SchemaVersion) -> None:
        if self.versions:
            previous = self.versions[-1]
            if not previous.is_compatible_with(version):
                raise ValueError(
                    f"version {version.version} is not compatible with {previous.version}"
                )
        self.versions.append(version)

    def latest(self) -> SchemaVersion:
        if not self.versions:
            raise LookupError("no schema versions registered")
        return self.versions[-1]
