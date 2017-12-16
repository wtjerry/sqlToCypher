from sqlToCypherConverter.Converter import Converter

if __name__ == "__main__":
    tables_to_convert = {
        'studenten': "MatrNr",
        'professoren': "PersNr",
        'assistenten': "PersNr",
        'vorlesungen': "VorlNr",
    }
    print(Converter().convert("./resources/05 uni-daten.sql", tables_to_convert, {}))
