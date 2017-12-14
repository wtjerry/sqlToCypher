import unittest

from sqlToCypherConverter.Converter import Converter


class ConverterTest(unittest.TestCase):
    def test_convert(self):
        result = Converter().convert("./../resources/insertInto.sql")
        expected = "CREATE (:STUDENTEN {MatrNr, Name, Semester})"
        self.assertEqual(expected, result)
