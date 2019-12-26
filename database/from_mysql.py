# Third party import
import pymysql

# Local import
from .utils import MySQL


class FromMySQL(MySQL):

    def __init__(self, info_dict, table, column):
        MySQL.__init__(self, table, column)
        self.info_dict = info_dict
        self.connection = self.connect()
        self.cursor = self.connection.cursor()
        self.pk = self.get_pk_name()

    def connect(self):
        connection = pymysql.connect(
            host=self.info_dict.get('HOST'),
            database=self.info_dict.get('DATABASE'),
            user=self.info_dict.get('USER'),
            password=self.info_dict.get('PASSWORD'),
            port=self.info_dict.get('PORT')
        )
        return connection

    def disconnect(self):
        if self.connection is not None and self.connection.open:
            self.connection.close()

    def get_pk_name(self):
        self.cursor.execute(self.select_pk_name_query())
        rows = self.cursor.fetchall()
        if len(rows) > 1:  # instead of self.cursor.rowcount for test ease
            msg = f"The table '{self.table}' contains more than one primary key"
            raise ValueError(msg)
        return rows[0][0]

    def select_duplicate(self, rows_list=False):
        if rows_list:
            self.cursor.execute(self.select_duplicate_query())
            return self.cursor.fetchall()

        self.cursor.execute(self.select_duplicate_pk_query(self.pk))
        return [row[0] for row in self.cursor.fetchall()]

    def select_unique(self, rows_list=False):
        if rows_list:
            self.cursor.execute(self.select_unique_query())
            return self.cursor.fetchall()

        self.cursor.execute(self.select_unique_pk_query(self.pk))
        return [row[0] for row in self.cursor.fetchall()]
