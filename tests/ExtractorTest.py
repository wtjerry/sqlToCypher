import unittest

from sqlToCypherConverter.Extractor import Extractor


class ConverterTest(unittest.TestCase):
    def test_extract_table(self):
        actual = Extractor("INSERT INTO studenten(MatrNr, Name, Semester)").extract_table()
        self.assertEqual("studenten", actual)
