from sqlToCypherConverter.Extractor import Extractor
from sqlToCypherConverter.constants import INSERT_INTO_STATEMENT


class Converter(object):

    def convert(self, sql):
        result = []

        with open(sql) as f:
            lines = f.readlines()
            for line in lines:
                line = line.lower()
                if INSERT_INTO_STATEMENT in line:
                    table_name = Extractor(line).extract_table()
                    statement = self._create_statement(table_name)
                    result.append(statement)

        return "\n".join(result)

    def _create_statement(self, table_name):
        return "CREATE (:{0})".format(table_name.upper())
