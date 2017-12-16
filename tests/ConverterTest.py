import unittest

from sqlToCypherConverter.Converter import Converter


class ConverterTest(unittest.TestCase):
    def test_convert_noTablesProvided_convertsEverything(self):
        result = Converter().convert("./../resources/insertInto.sql", [])
        expected = "CREATE (:STUDENTEN {MatrNr: 24002, Name: 'Xenokrates', Semester: 18})"
        self.assertEqual(expected, result)

    def test_convert_existingTableProvided_convertsThatTable(self):
        result = Converter().convert("./../resources/insertInto.sql", ['studenten'])
        expected = "CREATE (:STUDENTEN {MatrNr: 24002, Name: 'Xenokrates', Semester: 18})"
        self.assertEqual(expected, result)

    def test_convert_notExistingTableProvided_returnsNothing(self):
        result = Converter().convert("./../resources/insertInto.sql", ['professoren'])
        expected = ""
        self.assertEqual(expected, result)
