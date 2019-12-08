import unittest
import os

from copy import deepcopy
from dotenv import load_dotenv
from psycopg2 import DatabaseError

# Local import
from database.from_psql import FromPSQL
from test.database.fixtures.test_db import CreateDBs

load_dotenv()


class TestFromPSQL(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.psql_info_dict = {
            'HOST': os.getenv("POSTGRES_HOSTNAME"),
            'DATABASE': os.getenv("POSTGRES_DATABASE"),
            'USER': os.getenv("POSTGRES_USER"),
            'PASSWORD': os.getenv("POSTGRES_PASSWORD"),
            'PORT': os.getenv("POSTGRES_PORT"),
            'DEFAULT_DB': 'postgres',
        }
        CreateDBs(cls.psql_info_dict, 'psql')

    def setUp(self) -> None:
        self.info_dict = deepcopy(self.psql_info_dict)
        self.table = 'address'
        self.column = 'complete_address'

    def test_connect_and_disconnect_success(self):
        from_psql = FromPSQL(self.info_dict, self.table, self.column)
        self.assertFalse(from_psql.connection.closed)
        self.assertFalse(from_psql.cursor.closed)

        from_psql.disconnect()
        self.assertTrue(from_psql.connection.closed)
        self.assertTrue(from_psql.cursor.closed)

    def test_connect_error(self):
        self.info_dict['DATABASE'] = ''
        with self.assertRaises(DatabaseError):
            FromPSQL(self.info_dict, self.table, self.column)

    def test_select_duplicate(self):
        from_psql = FromPSQL(self.info_dict, self.table, self.column)

        result = from_psql.select_duplicate(rows_list=True)
        expected_result = [
            (2, '3 street test', 0, 2),
            (4, '5 street test', 1, 4),
            (5, '5 street test', 0, 3),
            (7, '3 street test', 0, 0)
        ]
        self.assertEqual(len(result), 4)
        self.assertEqual(result, expected_result)

        result = from_psql.select_duplicate()
        expected_result = [2, 4, 5, 7]
        self.assertEqual(len(result), 4)
        self.assertEqual(result, expected_result)

        from_psql.disconnect()

    def test_select_unique(self):
        from_psql = FromPSQL(self.info_dict, self.table, self.column)

        result = from_psql.select_unique(rows_list=True)
        expected_result = [
            (0, '1 street test', 0, 0),
            (1, '2 street test', 1, 1),
            (3, '4 street test', 0, 3),
            (6, '6 street test', 0, 4)
        ]
        self.assertEqual(len(result), 4)
        self.assertEqual(result, expected_result)

        result = from_psql.select_unique()
        expected_result = [0, 1, 3, 6]
        self.assertEqual(len(result), 4)
        self.assertEqual(result, expected_result)

        from_psql.disconnect()
