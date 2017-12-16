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
                'name': 'Student'
            }
        }
        result = Converter().convert("./../resources/insertInto.sql", tables_to_convert_to_nodes, {}, {})
        expected = "CREATE (_24002:Student {matrnr: 24002, name: 'Xenokrates', semester: 18})"
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
                'name': 'Vorlesungen'
            }
        }
        relationship_tables = {
            'voraussetzen': {
                'from': "Nachfolger",
                'to': "Vorgänger",
                'name': "SETZT_VORAUS"
            }
        }
        result = Converter().convert(
            "./../resources/insertInto_with_relationshipTable.sql",
            tables_to_convert_to_nodes,
            relationship_tables,
            {})
        expected = "CREATE (_5001:Vorlesungen {vorlnr: 5001, titel: 'Grundzuege', sws: 4, gelesenvon: 2137})" \
                   + "\n" \
                   + "CREATE (_5041:Vorlesungen {vorlnr: 5041, titel: 'Ethik', sws: 4, gelesenvon: 2125})" \
                   + "\n" \
                   + "CREATE (_5041) - [:SETZT_VORAUS] -> (_5001)"
        self.assertEqual(expected, result)

    def test_convert_existingTableANDspecialRelationshipTableProvided_convertsTableWithRelationship(self):
        tables_to_convert_to_nodes = {
            'vorlesungen': {
                'id_attribute': "VorlNr",
                'name': 'Vorlesungen'
            }
        }
        special_relationship_tables = {
            'vorlesungen': {
                'from': "VorlNr",
                'to': "gelesenVon",
                'name': "GELESEN_VON",
                'attribute_to_ignore_for_conversion': "gelesenVon"
            }
        }
        result = Converter().convert(
            "./../resources/insertInto_with_specialRelationship.sql",
            tables_to_convert_to_nodes,
            {},
            special_relationship_tables)
        expected = "CREATE (_5001:Vorlesungen {vorlnr: 5001, titel: 'Grundzuege', sws: 4})" \
                   + "\n" \
                   + "CREATE (_5001) - [:GELESEN_VON] -> (_2137)"
        self.assertEqual(expected, result)
