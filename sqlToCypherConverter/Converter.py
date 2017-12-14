class Converter(object):
    def convert(self, sql):
        result = []

        with open(sql) as f:
            lines = f.readlines()
            for l in lines:
                if "insert into" in l.lower():
                    result.append(l)

        return "\n".join(result)
