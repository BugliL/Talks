from unittest.mock import mock_open, patch
from unittest import TestCase


def read_file_content(filepath):
    """Funzione che legge un file e ritorna il contenuto"""
    with open(filepath, "r") as f:
        return f.read()


class TestFileRead(TestCase):
    @patch("builtins.open", mock_open(read_data="contenuto mockato del file"))
    def test_read_file_with_mock_open(self):
        """Esempio 1: Uso di mock_open per simulare lettura file"""

        content = read_file_content("file.txt")

        assert content == "contenuto mockato del file"
