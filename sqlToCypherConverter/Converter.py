from sqlToCypherConverter.Extractor import Extractor
from sqlToCypherConverter.constants import INSERT_INTO_STATEMENT


class Converter(object):

    def convert(self, sql):
        with open(sql) as f:
            lines = f.readlines()
            result = self.to_create_statement(lines)
        return "\n".join(result)

    def to_create_statement(self, lines):
        result = []
        for line in lines:
            if INSERT_INTO_STATEMENT in line.lower():
                extractor = Extractor(line)
                table_name = extractor.extract_table()
                columns = extractor.extract_columns()
                statement = self._create_statement(table_name, columns)
                result.append(statement)
        return result

    def _create_statement(self, table_name, columns):
        columns_comma_separated = ", ".join(columns)
        return "CREATE (:{0} {{{1}}})".format(table_name.upper(), columns_comma_separated)
