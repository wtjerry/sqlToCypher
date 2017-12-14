import unittest

from sqlToCypherConverter.Converter import Converter


class ConverterTest(unittest.TestCase):
    def test_convert(self):
        self.assertEqual("some sql", Converter().convert("some sql"))
