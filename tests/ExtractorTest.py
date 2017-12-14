import unittest

from sqlToCypherConverter.Extractor import Extractor


class ExtractorTest(unittest.TestCase):
    def test_extract_table(self):
        actual = Extractor("INSERT INTO studenten(MatrNr, Name, Semester)").extract_table()
        self.assertEqual("studenten", actual)

    def test_extract_columns(self):
        columns = Extractor("INSERT INTO studenten(MatrNr, Name, Semester)").extract_columns()

        expected = ["MatrNr", "Name", "Semester"]

        self.assertSequenceEqual(expected, columns)
