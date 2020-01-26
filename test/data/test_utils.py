import unittest

# Local import
from pyduplicate.data import const
from pyduplicate.data.utils import Utils
from test.data import test_const


class TestUtils(unittest.TestCase):

    def test_validate_items(self):
        # mixed list (and dict without key)
        for index, value in enumerate(test_const.LIST_ERROR):
            utils = Utils(value)
            utils.get_type()
            with self.assertRaises(TypeError):
                utils.validate_items()
        # mixed list of dict with key
        for index, value in enumerate(test_const.DICT_ERROR):
            utils = Utils(value)
            utils.create_list('id')
            utils.get_type()
            with self.assertRaises(TypeError):
                utils.validate_items()

    def test_create_unique_index_without_feedback(self):
        for index, value in enumerate(test_const.LIST):
            utils = Utils(value)
            indexes = utils.create_unique_index()
            self.assertEqual(
                indexes,
                test_const.LIST_CREATE_UNIQUE_INDEX[index]
            )

        for index, value in enumerate(test_const.DICT):
            utils = Utils(value)
            utils.create_list('id')
            indexes = utils.create_unique_index()
            self.assertEqual(
                indexes,
                test_const.DICT_CREATE_UNIQUE_INDEX[index]
            )

    def test_create_unique_index_with_feedback(self):
        for index, value in enumerate(test_const.LIST):
            utils = Utils(value)
            indexes = utils.create_unique_index(feedback=True)
            self.assertEqual(
                indexes,
                test_const.LIST_CREATE_UNIQUE_INDEX_FEEDBACK[index]
            )

        for index, value in enumerate(test_const.DICT):
            utils = Utils(value)
            utils.create_list('id')
            indexes = utils.create_unique_index(feedback=True)
            self.assertEqual(
                indexes,
                test_const.DICT_CREATE_UNIQUE_INDEX_WITH_FEEDBACK[index]
            )

    def test_get_indexes_unique_without_feedback(self):
        for index, value in enumerate(test_const.LIST):
            utils = Utils(value)
            indexes = utils.get_indexes(const.UNIQUE)
            self.assertEqual(
                indexes,
                test_const.LIST_GET_INDEXES_UNIQUE[index]
            )

        for index, value in enumerate(test_const.DICT):
            utils = Utils(value)
            utils.create_list('id')
            indexes = utils.get_indexes(const.UNIQUE)
            self.assertEqual(
                indexes,
                test_const.DICT_GET_INDEXES_UNIQUE[index]
            )

    def test_get_indexes_unique_with_feedback(self):
        for index, value in enumerate(test_const.LIST):
            utils = Utils(value)
            indexes = utils.get_indexes(const.UNIQUE, feedback=True)
            self.assertEqual(
                indexes,
                test_const.LIST_GET_INDEXES_UNIQUE_WITH_FEEDBACK[index]
            )

        for index, value in enumerate(test_const.DICT):
            utils = Utils(value)
            utils.create_list('id')
            indexes = utils.get_indexes(const.UNIQUE, feedback=True)
            self.assertEqual(
                indexes,
                test_const.DICT_GET_INDEXES_UNIQUE_WITH_FEEDBACK[index]
            )

    def test_get_indexes_duplicate_without_feedback(self):
        for index, value in enumerate(test_const.LIST):
            utils = Utils(value)
            indexes = utils.get_indexes(const.DUPLICATE)
            self.assertEqual(
                indexes,
                test_const.LIST_GET_INDEXES_DUPLICATE[index]
            )

        for index, value in enumerate(test_const.DICT):
            utils = Utils(value)
            utils.create_list('id')
            indexes = utils.get_indexes(const.DUPLICATE)
            self.assertEqual(
                indexes,
                test_const.DICT_GET_INDEXES_DUPLICATE[index]
            )

    def test_get_indexes_duplicate_with_feedback(self):
        for index, value in enumerate(test_const.LIST):
            utils = Utils(value)
            indexes = utils.get_indexes(const.DUPLICATE, feedback=True)
            self.assertEqual(
                indexes,
                test_const.LIST_GET_INDEXES_DUPLICATE_WITH_FEEDBACK[index]
            )

        for index, value in enumerate(test_const.DICT):
            utils = Utils(value)
            utils.create_list('id')
            indexes = utils.get_indexes(const.DUPLICATE, feedback=True)
            self.assertEqual(
                indexes,
                test_const.DICT_GET_INDEXES_DUPLICATE_WITH_FEEDBACK[index]
            )
