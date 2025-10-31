#!/usr/bin/env python3
"""
HW5: Fingerprint Processing - implement the `Fingerprint` class as described in README.md
"""
from typing import TypeVar

T = TypeVar("T", bound="Fingerprint")  # Generic type that must be a subclass of Fingerprint


class Fingerprint:
    """Class to represent a fingerprint with associated metadata."""

    match_threshold = 0.9

    def __init__(self, data: list[list[str]] | list[str], name: str, year: int, rows: int, cols: int) -> None:
        """
        Initialize a Fingerprint object with the given data and metadata.

        Arguments:
            data (list[list[str]]): 2D list representing the fingerprint pixels
            name (str): Name associated with the fingerprint
            year (int): Year the fingerprint was recorded
            rows (int): Number of rows in the fingerprint data
            cols (int): Number of columns in the fingerprint data
        """
        norm: list[list[str]] = []
        for r in range(rows):
            row = data[r] if r < len(data) else []
            row_chars = list(row) if isinstance(row, str) else list(row)
            row_chars = (row_chars + [""] * cols)[:cols]
            norm.append(row_chars)

        self._data = [row[:] for row in norm]
        self._name = name
        self._year = year
        self._rows = rows
        self._cols = cols

    @classmethod
    def from_file(cls: type[T], filename: str) -> T:
        """
        Create a Fingerprint object by reading fingerprint data from the file."""
        with open(filename, "r", encoding="utf-8") as f:
            name = f.readline().strip()
            year = int(f.readline().strip())
            rows = int(f.readline().strip())
            cols = int(f.readline().strip())
            chars: list[str] = []
            for line in f:
                for c in line:
                    if not c.isspace():
                        chars.append(c)
            data = [chars[i * cols:(i + 1) * cols] for i in range(rows)]
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
        a = self.image.replace("\n", "")
        b = other.image.replace("\n", "")
        total = self._rows * self._cols
        matches = sum(a[i] == b[i] for i in range(total))
        return matches / total >= self.match_threshold
