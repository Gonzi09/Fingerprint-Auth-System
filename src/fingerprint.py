#!/usr/bin/env python3
"""
HW5: Fingerprint Processing - implement the `Fingerprint` class as described in README.md
"""
from typing import TypeVar, Type

T = TypeVar("T", bound="Fingerprint")  # Generic type that must be a subclass of Fingerprint


class Fingerprint:
    match_threshold: float = 0.9

    def __init__(self, data: list[list[str]], name: str, year: int, rows: int, cols: int) -> None:
        self._data: list[list[str]] = [row[:] for row in data]
        self._name: str = name
        self._year: int = year
        self._rows: int = rows
        self._cols: int = cols

    @classmethod
    def from_file(cls: Type[T], filename: str) -> T:
        with open(filename, "r", encoding="utf-8") as f:
            name: str = f.readline().strip()
            year: int = int(f.readline().strip())
            rows: int = int(f.readline().strip())
            cols: int = int(f.readline().strip())
            chars: list[str] = [c for line in f for c in line if not c.isspace()]
        data: list[list[str]] = [chars[i * cols:(i + 1) * cols] for i in range(rows)]
        return cls(data, name, year, rows, cols)

    @property
    def image(self) -> str:
        return "\n".join("".join(row) for row in self._data)

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def cols(self) -> int:
        return self._cols

    @property
    def name(self) -> str:
        return self._name

    @property
    def year(self) -> int:
        return self._year

    def __str__(self) -> str:
        return f"Fingerprint for: {self._name}. Year recorded: {self._year}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Fingerprint):
            return False
        if self._rows != other._rows or self._cols != other._cols:
            return False
        a: str = self.image.replace("\n", "")
        b: str = other.image.replace("\n", "")
        total: int = min(len(a), len(b))
        matches: int = sum(a[i] == b[i] for i in range(total))
        return (matches / total) >= self.match_threshold