# Native import
import os
import unittest
from copy import deepcopy
from unittest import mock

# Third party import
from dotenv import load_dotenv
from pymysql import OperationalError

# Local import
from database.from_mysql import FromMySQL
from test.database.const import MYSQL
from test.database.fixtures.test_db import CreateFixtureDB

load_dotenv()


class TestFromMySQL(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        db_type = MYSQL
        cls.mysql_info_dict = {
            'HOST': os.getenv("MYSQL_HOSTNAME"),
            'DATABASE': os.getenv("MYSQL_DATABASE"),
            'USER': os.getenv("MYSQL_USER"),
            'PASSWORD': os.getenv("MYSQL_PASSWORD"),
            'PORT': int(os.getenv("MYSQL_PORT")),
        }
        cls.fixture = CreateFixtureDB(db_type, cls.mysql_info_dict)
        cls.fixture.create()

    def setUp(self) -> None:
        self.from_mysql = None
        self.info_dict = deepcopy(self.mysql_info_dict)
        self.table = 'address'
        self.column = 'complete_address'

    def tearDown(self) -> None:
        if self.from_mysql:
            self.from_mysql.disconnect()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.fixture.delete()

    def test_connect_and_disconnect_success(self):
        from_mysql = FromMySQL(self.info_dict, self.table, self.column)
        self.assertTrue(from_mysql.connection.open)

        from_mysql.disconnect()
        self.assertFalse(from_mysql.connection.open)

    def test_init_error(self):
        self.table = ['address']
        self.column = 'complete_address'
        with self.assertRaises(TypeError):
            FromMySQL(self.info_dict, self.table, self.column)

    def test_connect_error(self):
        # Tests for HOST / DATABASE / USER / PASSWORD / PORT are identical
        # and they should be handled by pymysql
        # So it's just an extra unnecessary test to catch a connection error
        self.info_dict['USER'] = 'ExistingUser'
        with self.assertRaises(OperationalError):
            FromMySQL(self.info_dict, self.table, self.column)

    def test_get_pk_name(self):
        self.from_mysql = FromMySQL(self.info_dict, self.table, self.column)
        self.assertEqual(self.from_mysql.pk, 'id')

    @mock.patch('pymysql.connect')
    def test_get_pk_name_error(self, mock_connect):
        mock_connect.return_value.cursor.return_value.fetchall.return_value = (
            ('id',), ('complete_address',)
        )
        with self.assertRaises(ValueError):
            FromMySQL(self.info_dict, self.table, self.column)

    def test_select_duplicate(self):
        self.from_mysql = FromMySQL(self.info_dict, self.table, self.column)

        result = self.from_mysql.select_duplicate(rows_list=True)
        expected_result = (
            (2, '3 street test', 0, 2),
            (4, '5 street test', 1, 4),
            (5, '5 street test', 0, 3),
            (7, '3 street test', 0, 0)
        )
        self.assertEqual(len(result), 4)
        self.assertCountEqual(result, expected_result)

        result = self.from_mysql.select_duplicate()
        expected_result = [2, 4, 5, 7]
        self.assertEqual(len(result), 4)
        self.assertCountEqual(result, expected_result)

    def test_select_unique(self):
        self.from_mysql = FromMySQL(self.info_dict, self.table, self.column)

        result = self.from_mysql.select_unique(rows_list=True)
        expected_result = (
            (0, '1 street test', 0, 0),
            (1, '2 street test', 1, 1),
            (3, '4 street test', 0, 3),
            (6, '6 street test', 0, 4)
        )
        self.assertEqual(len(result), 4)
        self.assertCountEqual(result, expected_result)

        result = self.from_mysql.select_unique()
        expected_result = [0, 1, 3, 6]
        self.assertEqual(len(result), 4)
        self.assertCountEqual(result, expected_result)
