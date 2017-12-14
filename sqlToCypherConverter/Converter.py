class Converter(object):
    INSERT_INTO_STATEMENT = "insert into"

    def convert(self, sql):
        result = []

        with open(sql) as f:
            lines = f.readlines()
            for line in lines:
                line = line.lower()
                if self.INSERT_INTO_STATEMENT in line:
                    table_name = self.__extract_table_name(line)
                    statement = self.__create_statement(table_name)
                    result.append(statement)

        return "\n".join(result)

    def __extract_table_name(self, line):
        start = line.index(self.INSERT_INTO_STATEMENT) + len(self.INSERT_INTO_STATEMENT) + 1
        end = line.index("(")
        table_name = line[start: end]
        return table_name

    def __create_statement(self, table_name):
        return "CREATE (:{0})".format(table_name.upper())
