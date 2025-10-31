import unittest
import sys
import os
from typing import Any

sys.path.append(".")
from src.fingerprint import Fingerprint


class TestFingerprint(unittest.TestCase):
    def setUp(self) -> None:
        '''Configuración base: imagen 2x3 y metadatos'''
        self.data: list[list[str]] = [
            ['#', '.', '#'],
            ['.', '#', '.'],
        ]
        self.name: str = "Mini"
        self.year: int = 2025
        self.rows: int = 2
        self.cols: int = 3

    def test_str_format(self) -> None:
        '''Verifica el formato exacto del __str__()'''
        fp: Fingerprint = Fingerprint(self.data, self.name, self.year, self.rows, self.cols)
        self.assertEqual(str(fp), "Fingerprint for: Mini. Year recorded: 2025")

    def test_properties_and_defensive_copy(self) -> None:
        '''Comprueba propiedades y que se haga copia defensiva del 2D-list'''
        fp: Fingerprint = Fingerprint(self.data, self.name, self.year, self.rows, self.cols)
        self.assertEqual(fp.rows, 2)
        self.assertEqual(fp.cols, 3)
        self.assertEqual(fp.name, "Mini")
        self.assertEqual(fp.year, 2025)

        '''Modificar el input no afecta al interno'''
        self.data[0][0] = 'X'
        self.assertEqual(fp.image[0][0], '#')

        '''image devuelve copia: cambiar la copia no cambia el interno'''
        img_copy: list[list[str]] = fp.image
        img_copy[0][0] = 'Z'
        self.assertEqual(fp.image[0][0], '#')

    def test_eq_true_at_or_above_threshold(self) -> None:
        '''Igualdad True cuando la similitud ≥ umbral'''
        Fingerprint.match_threshold = 0.8
        a: Fingerprint = Fingerprint(self.data, "A", 2024, 2, 3)
        b_data: list[list[str]] = [
            ['#', '.', '#'],
            ['.', '#', '#'],
        ]
        b: Fingerprint = Fingerprint(b_data, "B", 2024, 2, 3)
        self.assertTrue(a == b)

    def test_eq_false_below_threshold_or_size_mismatch(self) -> None:
        '''Igualdad False por similitud < umbral o por tamaño distinto'''
        Fingerprint.match_threshold = 0.9
        a: Fingerprint = Fingerprint(self.data, "A", 2024, 2, 3)
        b_data: list[list[str]] = [
            ['#', '.', '.'],
            ['.', '#', '.'],
        ]
        b: Fingerprint = Fingerprint(b_data, "B", 2024, 2, 3)
        self.assertFalse(a == b)

        '''Diferente tamaño debe ser False'''
        c: Fingerprint = Fingerprint([['#']], "C", 2024, 1, 1)
        self.assertFalse(a == c)

    def test_from_file_parses_and_ignores_whitespace(self) -> None:
        '''from_file() ignora whitespaces y arma la matriz correcta'''
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
