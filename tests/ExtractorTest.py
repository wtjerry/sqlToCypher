import unittest

from sqlToCypherConverter.Extractor import Extractor


class ExtractorTest(unittest.TestCase):
    def test_extract_table(self):
        actual = Extractor("INSERT INTO studenten(MatrNr, Name, Semester)").extract_table()
        self.assertEqual("studenten", actual)

    def test_extract_columns(self):
        columns = Extractor("INSERT INTO studenten(MatrNr, Name, Semester)\nVALUES (24002, 'Xenokrates', 18);")\
            .extract_columns()
        expected = {'MatrNr': 24002, 'Name': "Xenokrates", 'Semester': 18}
        self.assertDictEqual(expected, columns)
