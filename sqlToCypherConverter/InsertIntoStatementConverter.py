from sqlToCypherConverter.Extractor import Extractor


class InsertIntoStatementConverter(object):

    def to_node(self, sql_statement, tables_to_convert):
        extractor = Extractor(sql_statement)
        table_name = extractor.extract_table()
        columns = extractor.extract_columns()
        node_config = tables_to_convert[table_name]
        identifier = node_config['id_attribute']
        node_name = node_config['name']
        cypher_statement = self._create_node_statement(node_name, identifier, columns)
        return cypher_statement

    def to_relationship(self, sql_statement, relationship_tables):
        extractor = Extractor(sql_statement)
        table_name = extractor.extract_table()
        columns = extractor.extract_columns()
        rel = relationship_tables[table_name]
        relationship_name = rel['name']
        from_node_id = columns[rel['from']]
        to_node_id = columns[rel['to']]
        cypher_statement = self._create_relationship_statement(relationship_name, from_node_id, to_node_id)
        return cypher_statement

    def _get_identifier_name(self, table_name, tables_to_convert):
        return tables_to_convert[table_name]['id_attribute']

    def _create_node_statement(self, table_name, identifier_name, columns):
        formatted_columns = []
        for k, v in columns.items():
            if isinstance(v, str):
                formatted_columns.append("{0}: '{1}'".format(k, v))
            else:
                formatted_columns.append("{0}: {1}".format(k, v))

        identifier_value = columns[identifier_name]

        columns_string = ", ".join(formatted_columns)
        return "CREATE (_{0}:{1} {{{2}}})".format(identifier_value, table_name.upper(), columns_string)

    def _create_relationship_statement(self, table_name, from_node_id, to_node_id):
        return "CREATE (_{0}) - [:{1}] -> (_{2})".format(from_node_id, table_name.upper(), to_node_id)
