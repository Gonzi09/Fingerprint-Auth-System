#!/usr/bin/env python3
"""
HW5: Fingerprint Processing - implement the `Fingerprint` class as described in README.md
"""
from typing import TypeVar

T = TypeVar("T", bound="Fingerprint")  # Generic type that must be a subclass of Fingerprint


class Fingerprint:
    """Class to represent a fingerprint with associated metadata."""

    def __init__(self, data: list[list[str]], name: str, year: int, rows: int, cols: int) -> None:
        """
        Initialize a Fingerprint object with the given data and metadata.

        Arguments:
            data (list[list[str]]): 2D list representing the fingerprint pixels
            name (str): Name associated with the fingerprint
            year (int): Year the fingerprint was recorded
            rows (int): Number of rows in the fingerprint data
            cols (int): Number of columns in the fingerprint data
        """
        # Class variable default is defined below; store a copy of the data
        # Make a deep copy so external mutations don't affect the stored image
        self._image = [list(row) for row in data]
        self._name = name
        self._year = year
        self._rows = rows
        self._cols = cols

    # default match threshold (class variable)
    match_threshold: float = 0.9

    @classmethod
    def from_file(cls: type[T], filename: str) -> T:
        """
        Create a Fingerprint object by reading fingerprint data from the file."""
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()

        if len(lines) < 4:
            raise ValueError("Fingerprint file must contain at least 4 header lines")

        name = lines[0].strip()
        year = int(lines[1].strip())
        rows = int(lines[2].strip())
        cols = int(lines[3].strip())

        # Concatenate the rest of the lines and ignore all whitespace characters
        raw = "".join(lines[4:])
        chars = [c for c in raw if not c.isspace()]

        needed = rows * cols
        if len(chars) < needed:
            raise ValueError("Not enough pixel data in fingerprint file")

        # Build 2D list row-major
        data: list[list[str]] = []
        for r in range(rows):
            start = r * cols
            end = start + cols
            data.append(chars[start:end])

        return cls(data, name, year, rows, cols)

    # Properties
    @property
    def image(self) -> list[list[str]]:
        # Return a deep copy to prevent external mutation
        return [list(row) for row in self._image]

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
        # Return False if other is not a Fingerprint
        if not isinstance(other, Fingerprint):
            return False

        # Return False if rows/cols differ
        if self.rows != other.rows or self.cols != other.cols:
            return False

        # Compare pixel-by-pixel
        total = self.rows * self.cols
        equal = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self._image[r][c] == other._image[r][c]:
                    equal += 1

        percent = equal / total if total > 0 else 0.0

        return percent >= self.match_threshold
