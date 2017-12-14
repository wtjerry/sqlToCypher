from sqlToCypherConverter.constants import INSERT_INTO_STATEMENT, VALUES_KEYWORD
from collections import OrderedDict


class Extractor(object):

    def __init__(self, insert_into_statement):
        self._insert_into_statement = insert_into_statement

    def extract_table(self):
        start = self._insert_into_statement.lower().index(INSERT_INTO_STATEMENT) \
                + len(INSERT_INTO_STATEMENT) \
                + 1
        end = self._insert_into_statement.index("(")
        table_name = self._insert_into_statement[start: end]
        return table_name

    def extract_columns(self):
        column_names = self._extract_column_names()
        column_values = self._extract_column_values()
        columns = OrderedDict()
        for i, name in enumerate(column_names):
            columns.setdefault(name, column_values[i])
        return columns

    def _extract_column_names(self):
        column_names_string = self._get_column_names_string()
        return self._convert_to_column_names(column_names_string)

    def _get_column_names_string(self):
        start_names = self._insert_into_statement.index("(") + 1
        end_names = self._insert_into_statement.index(")")
        return self._insert_into_statement[start_names:end_names]

    def _convert_to_column_names(self, column_names_string):
        return [x.strip() for x in column_names_string.split(',')]

    def _extract_column_values(self):
        column_values_string = self._get_column_values_string()
        return self._convert_to_column_values(column_values_string)

    def _get_column_values_string(self):
        start_index_for_values = self._insert_into_statement.lower().index("{0} (".format(VALUES_KEYWORD))
        start_values = self._insert_into_statement.index("(", start_index_for_values) + 1
        end_values = self._insert_into_statement.index(")", start_index_for_values)
        return self._insert_into_statement[start_values:end_values]

    def _convert_to_column_values(self, column_values_string):
        column_values = []
        for cv in column_values_string.split(','):
            x = cv.strip()
            if x.isdigit():
                column_values.append(int(x))
            else:
                column_values.append(x[1:-1])
        return column_values
