from sqlToCypherConverter.InsertIntoStatementConverter import InsertIntoStatementConverter
from sqlToCypherConverter.constants import INSERT_INTO_STATEMENT


class Converter(object):

    def convert(self, sql_file, tables_to_convert_to_nodes, relationship_tables):
        with open(sql_file) as f:
            sql_statements = self._get_sql_statements(f)
            cypher_statements = self._convert_to_cypher_statements(
                sql_statements,
                tables_to_convert_to_nodes,
                relationship_tables)
        return "\n".join(cypher_statements)

    def _get_sql_statements(self, f):
        lines_as_string = "".join(f.readlines())
        sql_statements = lines_as_string.split(";")
        return sql_statements

    def _convert_to_cypher_statements(self, sql_statements, tables_to_convert_to_nodes, relationship_tables):
        cypher_statements = []
        for sql_statement in sql_statements:
            if self._is_insertInto(sql_statement):
                if self._should_convert_to_node(sql_statement, tables_to_convert_to_nodes.keys()):
                    cypher_statement = InsertIntoStatementConverter()\
                        .to_cypher(sql_statement, tables_to_convert_to_nodes)
                    cypher_statements.append(cypher_statement)
                elif any(x in sql_statement for x in relationship_tables.keys()):
                    cypher_statements.append("CREATE () - [] -> ()")

        return cypher_statements

    def _is_insertInto(self, sql_statement):
        return INSERT_INTO_STATEMENT in sql_statement.lower()

    def _should_convert_to_node(self, sql_statement, tables_to_convert):
        return any(x in sql_statement for x in tables_to_convert)
