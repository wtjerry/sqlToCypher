from sqlToCypherConverter.Extractor import Extractor


class InsertIntoStatementConverter(object):

    def to_node(self, sql_statement, tables_to_convert, foreign_key_relationship_tables):
        extractor = Extractor(sql_statement)
        table_name = extractor.extract_table()
        columns = extractor.extract_columns()

        columns = self._drop_ignored_columns(columns, foreign_key_relationship_tables, table_name)
        node_config = tables_to_convert[table_name]
        identifier = node_config['id_attribute']
        node_name = node_config['name']

        cypher_statement = self._create_node_statement(node_name, identifier, columns)
        return cypher_statement

    def to_relationship(self, sql_statement, many_to_many_relationship_tables):
        extractor = Extractor(sql_statement)
        table_name = extractor.extract_table()
        columns = extractor.extract_columns()

        rel = many_to_many_relationship_tables[table_name]
        relationship_name = rel['name']
        from_node_id = columns[rel['from']]
        to_node_id = columns[rel['to']]

        cypher_statement = self._create_relationship_statement(relationship_name, from_node_id, to_node_id)
        return cypher_statement

    def _drop_ignored_columns(self, columns, foreign_key_relationship_tables, table_name):
        if table_name in foreign_key_relationship_tables.keys():
            config = foreign_key_relationship_tables[table_name]['attribute_to_ignore_for_conversion']
            columns.pop(config)
        return columns

    def _create_node_statement(self, table_name, identifier_name, columns):
        formatted_columns = []
        for k, v in columns.items():
            if isinstance(v, str):
                formatted_columns.append("{0}: '{1}'".format(k.lower(), v))
            else:
                formatted_columns.append("{0}: {1}".format(k.lower(), v))

        identifier_value = columns[identifier_name]

        columns_string = ", ".join(formatted_columns)
        return "CREATE (_{0}:{1} {{{2}}})".format(identifier_value, table_name, columns_string)

    def _create_relationship_statement(self, table_name, from_node_id, to_node_id):
        return "CREATE (_{0}) - [:{1}] -> (_{2})".format(from_node_id, table_name.upper(), to_node_id)
