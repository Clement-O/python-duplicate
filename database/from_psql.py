import psycopg2

# Local import
from .utils import Utils


class FromPSQL(Utils):

    def __init__(self, info_dict):
        self.info_dict = info_dict
        self.connection = self.connect()
        self.cursor = None
        if self.connection is not None:
            self.cursor = self.connection.cursor()
        Utils.__init__(self, self.cursor)

    def connect(self):
        conn = psycopg2.connect(
            host=self.info_dict.get('HOST', "localhost"),
            database=self.info_dict.get('DATABASE'),
            user=self.info_dict.get('USER'),
            password=self.info_dict.get('PASSWORD'),
            port=self.info_dict.get('PORT', 5432),
        )
        return conn

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()
