# noinspection SqlNoDataSourceInspection,SqlDialectInspection
class Postgres:

    def __init__(self, table, column):
        self.table = table
        self.column = column
        if not all(isinstance(x, str) for x in [self.table, self.column]):
            raise TypeError(f"The 'table' and/or 'column' must be a string!")

    def select_pk_name_query(self):
        return f"SELECT a.attname " \
               f"FROM pg_index AS i " \
               f"JOIN pg_attribute AS a " \
               f"ON a.attrelid = i.indrelid " \
               f"AND a.attnum = ANY(i.indkey) " \
               f"WHERE  i.indrelid = '{self.table}'::regclass " \
               f"AND i.indisprimary;"

    def select_duplicate_query(self):
        return f"SELECT t.* " \
               f"FROM {self.table} AS t " \
               f"INNER JOIN (" \
               f"SELECT {self.column} " \
               f"FROM {self.table} " \
               f"GROUP BY {self.column} " \
               f"HAVING ( COUNT(*) > 1 )" \
               f") dt ON t.{self.column}=dt.{self.column}"

    def select_duplicate_pk_query(self, pk):
        return f"SELECT t.{pk} " \
               f"FROM {self.table} AS t " \
               f"INNER JOIN (" \
               f"SELECT {self.column} " \
               f"FROM {self.table} " \
               f"GROUP BY {self.column} " \
               f"HAVING ( COUNT(*) > 1 )" \
               f") dt ON t.{self.column}=dt.{self.column}"

    def select_unique_query(self):
        return f"SELECT t.* " \
               f"FROM {self.table} AS t " \
               f"INNER JOIN (" \
               f"SELECT {self.column} " \
               f"FROM {self.table} " \
               f"GROUP BY {self.column} " \
               f"HAVING ( COUNT(*) = 1 )" \
               f") dt ON t.{self.column}=dt.{self.column}"

    def select_unique_pk_query(self, pk):
        return f"SELECT t.{pk} " \
               f"FROM {self.table} AS t " \
               f"INNER JOIN (" \
               f"SELECT {self.column} " \
               f"FROM {self.table} " \
               f"GROUP BY {self.column} " \
               f"HAVING ( COUNT(*) = 1 )" \
               f") dt ON t.{self.column}=dt.{self.column}"


# noinspection SqlNoDataSourceInspection,SqlDialectInspection
class MySQL:

    def __init__(self, table, column):
        self.table = table
        self.column = column
        if not all(isinstance(x, str) for x in [self.table, self.column]):
            raise TypeError(f"The 'table' and/or 'column' must be a string!")

    def select_pk_name_query(self):
        return f"SELECT k.COLUMN_NAME " \
               f"FROM information_schema.table_constraints t " \
               f"LEFT JOIN information_schema.key_column_usage k " \
               f"USING(constraint_name,table_schema,table_name) " \
               f"WHERE t.constraint_type='PRIMARY KEY' " \
               f"AND t.table_schema=DATABASE() " \
               f"AND t.table_name='{self.table}'"

    def select_duplicate_query(self):
        return f"SELECT t.* " \
               f"FROM {self.table} AS t " \
               f"INNER JOIN (" \
               f"SELECT {self.column} " \
               f"FROM {self.table} " \
               f"GROUP BY {self.column} " \
               f"HAVING ( COUNT(*) > 1 )" \
               f") dt ON t.{self.column}=dt.{self.column}"

    def select_duplicate_pk_query(self, pk):
        return f"SELECT t.{pk} " \
               f"FROM {self.table} AS t " \
               f"INNER JOIN (" \
               f"SELECT {self.column} " \
               f"FROM {self.table} " \
               f"GROUP BY {self.column} " \
               f"HAVING ( COUNT(*) > 1 )" \
               f") dt ON t.{self.column}=dt.{self.column}"

    def select_unique_query(self):
        return f"SELECT t.* " \
               f"FROM {self.table} AS t " \
               f"INNER JOIN (" \
               f"SELECT {self.column} " \
               f"FROM {self.table} " \
               f"GROUP BY {self.column} " \
               f"HAVING ( COUNT(*) = 1 )" \
               f") dt ON t.{self.column}=dt.{self.column}"

    def select_unique_pk_query(self, pk):
        return f"SELECT t.{pk} " \
               f"FROM {self.table} AS t " \
               f"INNER JOIN (" \
               f"SELECT {self.column} " \
               f"FROM {self.table} " \
               f"GROUP BY {self.column} " \
               f"HAVING ( COUNT(*) = 1 )" \
               f") dt ON t.{self.column}=dt.{self.column}"
