from sqlToCypherConverter.Converter import Converter

if __name__ == "__main__":
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
    tables_to_convert = {
        'studenten': "MatrNr",
        'professoren': "PersNr",
        'vorlesungen': "VorlNr",
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
        tables_to_convert,
        relationship_tables,
        special_relationship_tables))
