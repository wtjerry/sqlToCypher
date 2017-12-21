from sqlToCypherConverter.InsertIntoStatementConverter import InsertIntoStatementConverter
from sqlToCypherConverter.constants import INSERT_INTO_STATEMENT


class Converter(object):

    def __init__(self, sql_file, tables_to_convert_to_nodes, relationship_tables, special_relationship_tables):
        self.sql_file = sql_file
        self.tables_to_convert_to_nodes = tables_to_convert_to_nodes
        self.many_to_many_relationship_tables = relationship_tables
        self.foreign_key_relationship_tables = special_relationship_tables

    def convert(self, ):
        with open(self.sql_file) as f:
            sql_statements = self._get_sql_statements(f)
            cypher_statements = self._convert_to_cypher_statements(sql_statements)
        return "\n".join(cypher_statements)

    def _get_sql_statements(self, f):
        lines_as_string = "".join(f.readlines())
        sql_statements = lines_as_string.split(";")
        return sql_statements

    def _convert_to_cypher_statements(self, sql_statements):
        cypher_statements = []
        for sql_statement in sql_statements:
            if self._is_insertInto(sql_statement):
                if self._should_convert_to_node(sql_statement):
                    cypher_statements.append(self._create_node(sql_statement))
                    if self._is_foreign_key_table(sql_statement):
                        cypher_statements.append(self._create_relationship_from_foreign_key_table(sql_statement))
                elif self._is_many_to_many_table(sql_statement):
                    cypher_statements.append(self._create_relationship_from_many_to_many_table(sql_statement))
        return cypher_statements

    def _is_insertInto(self, sql_statement):
        return INSERT_INTO_STATEMENT in sql_statement.lower()

    def _should_convert_to_node(self, sql_statement):
        return any(x in sql_statement for x in self.tables_to_convert_to_nodes.keys())

    def _create_node(self, sql_statement):
        return InsertIntoStatementConverter() \
            .to_node(sql_statement, self.tables_to_convert_to_nodes, self.foreign_key_relationship_tables)

    def _is_foreign_key_table(self, sql_statement):
        return any(x in sql_statement for x in self.foreign_key_relationship_tables)

    def _create_relationship_from_foreign_key_table(self, sql_statement):
        return InsertIntoStatementConverter() \
            .to_relationship(sql_statement, self.foreign_key_relationship_tables)

    def _is_many_to_many_table(self, sql_statement):
        return any(x in sql_statement for x in self.many_to_many_relationship_tables.keys())

    def _create_relationship_from_many_to_many_table(self, sql_statement):
        return InsertIntoStatementConverter() \
            .to_relationship(sql_statement, self.many_to_many_relationship_tables)
