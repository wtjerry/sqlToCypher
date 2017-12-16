import unittest

from sqlToCypherConverter.Converter import Converter


class ConverterTest(unittest.TestCase):
    def test_convert_noTablesProvided_returnsNothing(self):
        result = Converter().convert("./../resources/insertInto.sql", {}, {})
        expected = ""
        self.assertEqual(expected, result)

    def test_convert_existingTableProvided_convertsThatTable(self):
        tables_to_converttables_to_convert_to_nodes = {'studenten': "MatrNr"}
        result = Converter().convert("./../resources/insertInto.sql", tables_to_converttables_to_convert_to_nodes, {})
        expected = "CREATE (24002:STUDENTEN {MatrNr: 24002, Name: 'Xenokrates', Semester: 18})"
        self.assertEqual(expected, result)

    def test_convert_notExistingTableProvided_returnsNothing(self):
        result = Converter().convert("./../resources/insertInto.sql", {'professoren': "PersNr"}, {})
        expected = ""
        self.assertEqual(expected, result)

    def test_convert_existingTableANDrelationshipTableProvided_convertsTableWithDummyRelationship(self):
        tables_to_convert_to_nodes = {'vorlesungen': "VorlNr"}
        relationship_tables = {
            'voraussetzen': {
                'from': {
                    'attribute_name': "Nachfolger",
                    'table_name': "vorlesungen"
                },
                'to': {
                    'attribute_name': "Vorgänger",
                    'table_name': "vorlesungen"
                }
            }
        }
        result = Converter()\
            .convert("./../resources/insertInto_with_relationshipTable.sql", tables_to_convert_to_nodes, relationship_tables)
        expected = "CREATE (5001:VORLESUNGEN {VorlNr: 5001, Titel: 'Grundzuege', SWS: 4, gelesenVon: 2137})" \
                   + "\n" \
                   + "CREATE (5041:VORLESUNGEN {VorlNr: 5041, Titel: 'Ethik', SWS: 4, gelesenVon: 2125})" \
                   + "\n" \
                   + "CREATE () - [:VORAUSSETZEN] -> ()"
        self.assertEqual(expected, result)
