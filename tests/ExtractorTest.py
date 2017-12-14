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

    def test_extract_columns_with_decimals(self):
        columns = Extractor("INSERT INTO pruefen(MatrNr, VorlNr, PersNr, Note)\nVALUES (27550, 4630, 2137, 2.0));") \
            .extract_columns()
        expected = {'MatrNr': 27550, 'VorlNr': 4630, 'PersNr': 2137, 'Note': 2.0}
        self.assertDictEqual(expected, columns)

