import unittest
from psycopg2 import DatabaseError

# Local import
from database.from_psql import FromPSQL
from test.database import test_const


class TestFromPSQL(unittest.TestCase):

    def setUp(self) -> None:
        self.info_dict = {
            'HOST': test_const.POSTGRES_HOSTNAME,
            'DATABASE': test_const.POSTGRES_DATABASE,
            'USER': test_const.POSTGRES_USER,
            'PASSWORD': test_const.POSTGRES_PASSWORD,
            'PORT': test_const.POSTGRES_PORT,
        }

    def test_connect_and_disconnect_success(self):
        from_psql = FromPSQL(self.info_dict)
        self.assertFalse(from_psql.connection.closed)
        self.assertFalse(from_psql.cursor.closed)
        from_psql.disconnect()
        self.assertTrue(from_psql.connection.closed)
        self.assertTrue(from_psql.cursor.closed)

    def test_connect_error(self):
        self.info_dict['DATABASE'] = ''
        with self.assertRaises(DatabaseError):
            FromPSQL(self.info_dict)
