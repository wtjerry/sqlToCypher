import unittest

from sqlToCypherConverter.Converter import Converter


class ConverterTest(unittest.TestCase):
    def test_convert_noTablesProvided_returnsNothing(self):
        result = Converter().convert("./../resources/insertInto.sql", {}, {}, {})
        expected = ""
        self.assertEqual(expected, result)

    def test_convert_existingTableProvided_convertsThatTable(self):
        tables_to_convert_to_nodes = {
            'studenten': {
                'id_attribute': "MatrNr",
                'name': 'student'
            }
        }
        result = Converter().convert("./../resources/insertInto.sql", tables_to_convert_to_nodes, {}, {})
        expected = "CREATE (_24002:STUDENT {MatrNr: 24002, Name: 'Xenokrates', Semester: 18})"
        self.assertEqual(expected, result)

    def test_convert_notExistingTableProvided_returnsNothing(self):
        tables_to_convert_to_nodes = {'professoren': {}}
        result = Converter().convert("./../resources/insertInto.sql", tables_to_convert_to_nodes, {}, {})
        expected = ""
        self.assertEqual(expected, result)

    def test_convert_existingTableANDrelationshipTableProvided_convertsTableWithRelationship(self):
        tables_to_convert_to_nodes = {
            'vorlesungen': {
                'id_attribute': "VorlNr",
                'name': 'vorlesungen'
            }
        }
        relationship_tables = {
            'voraussetzen': {
                'from': "Nachfolger",
                'to': "Vorgänger",
                'name': "setzt_voraus"
            }
        }
        result = Converter().convert(
            "./../resources/insertInto_with_relationshipTable.sql",
            tables_to_convert_to_nodes,
            relationship_tables,
            {})
        expected = "CREATE (_5001:VORLESUNGEN {VorlNr: 5001, Titel: 'Grundzuege', SWS: 4, gelesenVon: 2137})" \
                   + "\n" \
                   + "CREATE (_5041:VORLESUNGEN {VorlNr: 5041, Titel: 'Ethik', SWS: 4, gelesenVon: 2125})" \
                   + "\n" \
                   + "CREATE (_5041) - [:SETZT_VORAUS] -> (_5001)"
        self.assertEqual(expected, result)

    def test_convert_existingTableANDspecialRelationshipTableProvided_convertsTableWithRelationship(self):
        tables_to_convert_to_nodes = {
            'vorlesungen': {
                'id_attribute': "VorlNr",
                'name': 'vorlesungen'
            }
        }
        special_relationship_tables = {
            'vorlesungen': {
                'from': "VorlNr",
                'to': "gelesenVon",
                'name': "gelesenVon"
            }
        }
        result = Converter().convert(
            "./../resources/insertInto_with_specialRelationship.sql",
            tables_to_convert_to_nodes,
            {},
            special_relationship_tables)
        expected = "CREATE (_5001:VORLESUNGEN {VorlNr: 5001, Titel: 'Grundzuege', SWS: 4, gelesenVon: 2137})" \
                   + "\n" \
                   + "CREATE (_5001) - [:GELESENVON] -> (_2137)"
        self.assertEqual(expected, result)
