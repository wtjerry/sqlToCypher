from sqlToCypherConverter.Converter import Converter

if __name__ == "__main__":
    tables_to_convert_to_nodes = {
        'studenten': {
            'id_attribute': "MatrNr",
            'name': 'student'
        },
        'professoren': {
            'id_attribute': "PersNr",
            'name': 'professor'
        },
        'vorlesungen': {
            'id_attribute': "VorlNr",
            'name': 'vorlesung'
        }
    }
    relationship_tables = {
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
    special_relationship_tables = {
        'vorlesungen': {
            'from': "gelesenVon",
            'to': "VorlNr",
            'name': "liest"
        }
    }
    print(Converter().convert(
        "./resources/05 uni-daten.sql",
        tables_to_convert_to_nodes,
        relationship_tables,
        special_relationship_tables))
