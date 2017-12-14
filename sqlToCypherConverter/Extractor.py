from sqlToCypherConverter.constants import INSERT_INTO_STATEMENT


class Extractor(object):

    def __init__(self, insert_into_statement):
        self._insert_into_statement = insert_into_statement

    def extract_table(self):
        start = self._insert_into_statement.lower().index(INSERT_INTO_STATEMENT) \
                + len(INSERT_INTO_STATEMENT) \
                + 1
        end = self._insert_into_statement.lower().index("(")
        table_name = self._insert_into_statement[start: end]
        return table_name
