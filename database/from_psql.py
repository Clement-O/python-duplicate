import psycopg2

# Local import
from .utils import Utils


class FromPSQL(Utils):

    def __init__(self, info_dict, table, column):
        Utils.__init__(self, table, column)
        self.info_dict = info_dict
        self.connection = self.connect()
        self.cursor = self.connection.cursor()
        self.pk = self.get_pk_name()

    def connect(self):
        connection = psycopg2.connect(
            host=self.info_dict.get('HOST', 'localhost'),
            database=self.info_dict.get('DATABASE'),
            user=self.info_dict.get('USER'),
            password=self.info_dict.get('PASSWORD'),
            port=self.info_dict.get('PORT', 5432),
        )
        return connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def get_pk_name(self):
        self.cursor.execute(self.postgres.select_primary_key_name_query())
        row = self.cursor.fetchone()
        return row[0]

    def select_duplicate(self, rows_list=False):
        if rows_list:
            self.cursor.execute(self.postgres.select_duplicate_query())
            return self.cursor.fetchall()

        self.cursor.execute(self.postgres.select_duplicate_pk_query(self.pk))
        return [row[0] for row in self.cursor.fetchall()]

    def select_unique(self, rows_list=False):
        if rows_list:
            self.cursor.execute(self.postgres.select_unique_query())
            return self.cursor.fetchall()

        self.cursor.execute(self.postgres.select_unique_pk_query(self.pk))
        return [row[0] for row in self.cursor.fetchall()]
