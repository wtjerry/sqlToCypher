import unittest

from sqlToCypherConverter.Converter import Converter


# noinspection SqlNoDataSourceInspection
class ConverterTest(unittest.TestCase):
    def test_convert(self):
        result = Converter().convert("./../resources/insertInto.sql")
        expected = "INSERT INTO studenten(MatrNr, Name, Semester) \n"
        self.assertEqual(expected, result)
