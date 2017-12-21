from sqlToCypherConverter.Converter import Converter

if __name__ == "__main__":
    tables_to_convert_to_nodes = {
        'studenten': {
            'id_attribute': "MatrNr",
            'name': 'Student'
        },
        'professoren': {
            'id_attribute': "PersNr",
            'name': 'Professor'
        },
        'vorlesungen': {
            'id_attribute': "VorlNr",
            'name': 'Vorlesung'
        }
    }
    many_to_many_relationship_tables = {
        'voraussetzen': {
            'from': "Nachfolger",
            'to': "Vorgänger",
            'name': "setzt_voraus"
        },
        'hoeren': {
            'from': "MatrNr",
            'to': "VorlNr",
            'name': "hoert"
        }
    }
    foreign_key_relationship_tables = {
        'vorlesungen': {
            'from': "gelesenVon",
            'to': "VorlNr",
            'name': "liest",
            'attribute_to_ignore_for_conversion': "gelesenVon"
        }
    }

    converter = Converter(
        "./resources/05 uni-daten.sql",
        tables_to_convert_to_nodes,
        many_to_many_relationship_tables,
        foreign_key_relationship_tables)
    print(converter.convert())
