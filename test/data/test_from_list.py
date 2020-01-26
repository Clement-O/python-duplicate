import unittest

# Local import
from pyduplicate.data import const
from pyduplicate import FromList
from test.data import test_const


class TestFromList(unittest.TestCase):

    def test_analyze_without_feedback(self):
        for index, value in enumerate(test_const.LIST):
            from_list = FromList(value)
            analyze = from_list.analyze(const.UNIQUE, False)
            self.assertEqual(
                analyze,
                test_const.LIST_GET_INDEXES_UNIQUE[index]
            )

            from_list = FromList(value)
            analyze = from_list.analyze(const.DUPLICATE, False)
            self.assertEqual(
                analyze,
                test_const.LIST_GET_INDEXES_DUPLICATE[index]
            )

            from_list = FromList(value)
            analyze = from_list.analyze(const.CREATE_UNIQUE, False)
            self.assertEqual(
                analyze,
                test_const.LIST_CREATE_UNIQUE_INDEX[index]
            )

        for index, value in enumerate(test_const.DICT):
            from_list = FromList(value, 'id')
            analyze = from_list.analyze(const.UNIQUE, False)
            self.assertEqual(
                analyze,
                test_const.DICT_GET_INDEXES_UNIQUE[index]
            )

            from_list = FromList(value, 'id')
            analyze = from_list.analyze(const.DUPLICATE, False)
            self.assertEqual(
                analyze,
                test_const.DICT_GET_INDEXES_DUPLICATE[index]
            )

            from_list = FromList(value, 'id')
            analyze = from_list.analyze(const.CREATE_UNIQUE, False)
            self.assertEqual(
                analyze,
                test_const.DICT_CREATE_UNIQUE_INDEX[index]
            )

    def test_analyze_with_feedback(self):
        for index, value in enumerate(test_const.LIST):
            from_list = FromList(value)
            analyze = from_list.analyze(const.UNIQUE)
            self.assertEqual(
                analyze,
                test_const.LIST_GET_INDEXES_UNIQUE_WITH_FEEDBACK[index]
            )

            from_list = FromList(value)
            analyze = from_list.analyze(const.DUPLICATE)
            self.assertEqual(
                analyze,
                test_const.LIST_GET_INDEXES_DUPLICATE_WITH_FEEDBACK[index]
            )

            from_list = FromList(value)
            analyze = from_list.analyze(const.CREATE_UNIQUE)
            self.assertEqual(
                analyze,
                test_const.LIST_CREATE_UNIQUE_INDEX_FEEDBACK[index]
            )

        for index, value in enumerate(test_const.DICT):
            from_list = FromList(value, 'id')
            analyze = from_list.analyze(const.UNIQUE)
            self.assertEqual(
                analyze,
                test_const.DICT_GET_INDEXES_UNIQUE_WITH_FEEDBACK[index]
            )

            from_list = FromList(value, 'id')
            analyze = from_list.analyze(const.DUPLICATE)
            self.assertEqual(
                analyze,
                test_const.DICT_GET_INDEXES_DUPLICATE_WITH_FEEDBACK[index]
            )

            from_list = FromList(value, 'id')
            analyze = from_list.analyze(const.CREATE_UNIQUE)
            self.assertEqual(
                analyze,
                test_const.DICT_CREATE_UNIQUE_INDEX_WITH_FEEDBACK[index]
            )

    def test_create_unique(self):
        for index, value in enumerate(test_const.LIST):
            from_list = FromList(value)
            analyze = from_list.create_unique()
            self.assertEqual(
                analyze,
                test_const.LIST_CREATE_UNIQUE[index]
            )

        for index, value in enumerate(test_const.DICT):
            from_list = FromList(value, 'id')
            analyze = from_list.create_unique()
            self.assertEqual(
                analyze,
                test_const.DICT_CREATE_UNIQUE[index]
            )

    def test_get_unique(self):
        for index, value in enumerate(test_const.LIST):
            from_list = FromList(value)
            analyze = from_list.get_unique()
            self.assertEqual(
                analyze,
                test_const.LIST_GET_UNIQUE[index]
            )

        for index, value in enumerate(test_const.DICT):
            from_list = FromList(value, 'id')
            analyze = from_list.get_unique()
            self.assertEqual(
                analyze,
                test_const.DICT_GET_UNIQUE[index]
            )

    def test_get_duplicate(self):
        for index, value in enumerate(test_const.LIST):
            from_list = FromList(value)
            analyze = from_list.get_duplicate()
            self.assertEqual(
                analyze,
                test_const.LIST_GET_DUPLICATE[index]
            )

        for index, value in enumerate(test_const.DICT):
            from_list = FromList(value, 'id')
            analyze = from_list.get_duplicate()
            self.assertEqual(
                analyze,
                test_const.DICT_GET_DUPLICATE[index]
            )
