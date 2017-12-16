from sqlToCypherConverter.Extractor import Extractor
from sqlToCypherConverter.constants import INSERT_INTO_STATEMENT


class Converter(object):

    def convert(self, sql_file, tables_to_convert):
        with open(sql_file) as f:
            s = "".join(f.readlines())
            result = self.to_create_statement(s, tables_to_convert)
        return "".join(result)

    def to_create_statement(self, s, tables_to_convert):
        result = []
        for sql_statement in s.split(";"):
            if self._is_insertInto(sql_statement) and self._should_convert(sql_statement, tables_to_convert):
                extractor = Extractor(sql_statement)
                table_name = extractor.extract_table()
                columns = extractor.extract_columns()
                cypher_statement = self._create_statement(table_name, columns)
                result.append(cypher_statement)
        return "\n".join(result)

    def _is_insertInto(self, sql_statement):
        return INSERT_INTO_STATEMENT in sql_statement.lower()

    def _should_convert(self, sql_statement, tables_to_convert):
        if not tables_to_convert:
            return True
        return any(x in sql_statement for x in tables_to_convert)

    def _create_statement(self, table_name, columns):
        formatted_columns = []
        for k, v in columns.items():
            if isinstance(v, str):
                formatted_columns.append("{0}: '{1}'".format(k, v))
            else:
                formatted_columns.append("{0}: {1}".format(k, v))

        columns_string = ", ".join(formatted_columns)
        return "CREATE (:{0} {{{1}}})".format(table_name.upper(), columns_string)
