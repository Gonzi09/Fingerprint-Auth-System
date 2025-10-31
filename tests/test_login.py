import unittest
import sys
import os
from typing import Any

sys.path.append(".")
from src.fingerprint import Fingerprint


class TestFingerprint(unittest.TestCase):
    def setUp(self) -> None:
        """Basic setup: 2x3 fingerprint image and metadata"""
        self.data: list[list[str]] = [
            ['#', '.', '#'],
            ['.', '#', '.'],
        ]
        self.name: str = "Mini"
        self.year: int = 2025
        self.rows: int = 2
        self.cols: int = 3

    def test_str_format(self) -> None:
        """Checks that __str__() returns the correct formatted string"""
        fp: Fingerprint = Fingerprint(self.data, self.name, self.year, self.rows, self.cols)
        self.assertEqual(str(fp), "Fingerprint for: Mini. Year recorded: 2025")

    def test_properties_and_defensive_copy(self) -> None:
        """Verifies properties and defensive copying of internal data"""
        fp: Fingerprint = Fingerprint(self.data, self.name, self.year, self.rows, self.cols)
        self.assertEqual(fp.rows, 2)
        self.assertEqual(fp.cols, 3)
        self.assertEqual(fp.name, "Mini")
        self.assertEqual(fp.year, 2025)

        """Changing the original input should not affect internal data"""
        self.data[0][0] = 'X'
        self.assertEqual(fp.image[0][0], '#')

        """Changing the image copy should not affect the internal data"""
        img_copy: list[list[str]] = fp.image
        img_copy[0][0] = 'Z'
        self.assertEqual(fp.image[0][0], '#')

    def test_eq_true_at_or_above_threshold(self) -> None:
        """Equality should be True when similarity is at or above the threshold"""
        Fingerprint.match_threshold = 0.8
        a: Fingerprint = Fingerprint(self.data, "A", 2024, 2, 3)
        b_data: list[list[str]] = [
            ['#', '.', '#'],
            ['.', '#', '#'],
        ]
        b: Fingerprint = Fingerprint(b_data, "B", 2024, 2, 3)
        self.assertTrue(a == b)

    def test_eq_false_below_threshold_or_size_mismatch(self) -> None:
        """Equality should be False when similarity is below threshold or sizes differ"""
        Fingerprint.match_threshold = 0.9
        a: Fingerprint = Fingerprint(self.data, "A", 2024, 2, 3)
        b_data: list[list[str]] = [
            ['#', '.', '.'],
            ['.', '#', '.'],
        ]
        b: Fingerprint = Fingerprint(b_data, "B", 2024, 2, 3)
        self.assertFalse(a == b)

        """Different sizes should also result in False"""
        c: Fingerprint = Fingerprint([['#']], "C", 2024, 1, 1)
        self.assertFalse(a == c)

    def test_from_file_parses_and_ignores_whitespace(self) -> None:
        """Checks that from_file() correctly reads and ignores whitespace"""
        content: str = (
            "Mini\n"
            "2025\n"
            "2\n"
            "3\n"
            "# . #  \n"
            " . # .\n"
        )
        path: str = "test_fingerprint_input.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        try:
            fp: Fingerprint = Fingerprint.from_file(path)
            self.assertEqual(fp.name, "Mini")
            self.assertEqual(fp.year, 2025)
            self.assertEqual(fp.rows, 2)
            self.assertEqual(fp.cols, 3)
            self.assertEqual(fp.image, self.data)
        finally:
            if os.path.exists(path):
                os.remove(path)


if __name__ == "__main__":
    unittest.main()
