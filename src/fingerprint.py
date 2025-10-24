#!/usr/bin/env python3
"""
HW5: Fingerprint Processing - implement the `Fingerprint` class as described in README.md
"""
from typing import TypeVar

T = TypeVar(
    "T", bound="Fingerprint"
)  # Generic type that must be a subclass of Fingerprint


class Fingerprint:
    """Class to represent a fingerprint with associated metadata."""

    def __init__(
        self, data: list[list[str]], name: str, year: int, rows: int, cols: int
    ) -> None:
        """
        Initialize a Fingerprint object with the given data and metadata.

        Arguments:
            data (list[list[str]]): 2D list representing the fingerprint pixels
            name (str): Name associated with the fingerprint
            year (int): Year the fingerprint was recorded
            rows (int): Number of rows in the fingerprint data
            cols (int): Number of columns in the fingerprint data
        """
        pass

    @classmethod
    def from_file(cls: type[T], filename: str) -> T:
        """
        Create a Fingerprint object by reading fingerprint data from the file."""
        pass
