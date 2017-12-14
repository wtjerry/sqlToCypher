from sqlToCypherConverter.Extractor import Extractor
from sqlToCypherConverter.constants import INSERT_INTO_STATEMENT


class Converter(object):

    def convert(self, sql):
        with open(sql) as f:
            s = "".join(f.readlines())
            result = self.to_create_statement(s)
        return "".join(result)

    def to_create_statement(self, s):
        result = []
        for sql_statement in s.split(";"):
            if INSERT_INTO_STATEMENT in sql_statement.lower():
                extractor = Extractor(sql_statement)
                table_name = extractor.extract_table()
                columns = extractor.extract_columns()
                cypher_statement = self._create_statement(table_name, columns)
                result.append(cypher_statement)
        return "\n".join(result)

    def _create_statement(self, table_name, columns):
        formatted_columns = []
        for k, v in columns.items():
            if isinstance(v, str):
                formatted_columns.append("{0}: '{1}'".format(k, v))
            else:
                formatted_columns.append("{0}: {1}".format(k, v))

        columns_string = ", ".join(formatted_columns)
        return "CREATE (:{0} {{{1}}})".format(table_name.upper(), columns_string)
