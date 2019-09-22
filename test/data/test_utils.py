import unittest
# Local import
import const
from data.utils import Utils


class TestUtils(unittest.TestCase):

    def test_get_information_ok(self):
        # list (and dict without key)
        for index, value in enumerate(const.LIST):
            items_type = Utils.get_type(value[0])
            self.assertEqual(
                Utils.get_information(value, items_type),
                const.LIST_GET_INFORMATION[index]
            )
        # list of dict with key
        for index, value in enumerate(const.DICT):
            created_list = Utils.create_list(value, 'id')
            items_type = Utils.get_type(created_list[0])
            self.assertEqual(
                Utils.get_information(created_list, items_type),
                const.DICT_GET_INFORMATION[index])

    def test_get_information_error(self):
        # mixed list (and dict without key)
        for index, value in enumerate(const.LIST_ERROR):
            items_type = Utils.get_type(value[0])
            with self.assertRaises(TypeError):
                Utils.get_information(value, items_type)
        # mixed list of dict with key
        for index, value in enumerate(const.DICT_ERROR):
            created_list = Utils.create_list(value, 'id')
            items_type = Utils.get_type(created_list[0])
            with self.assertRaises(TypeError):
                Utils.get_information(created_list, items_type)

    def test_duplicate_list_without_feedback(self):
        for index, value in enumerate(const.LIST):
            duplicate_list = Utils.duplicate_list(value)
            self.assertEqual(
                duplicate_list,
                const.LIST_DUPLICATE_LIST[index]
            )

        for index, value in enumerate(const.DICT):
            created_list = Utils.create_list(value, 'id')
            duplicate_list = Utils.duplicate_list(created_list)
            self.assertEqual(
                duplicate_list,
                const.DICT_DUPLICATE_LIST[index]
            )

    def test_duplicate_list_with_feedback(self):
        for index, value in enumerate(const.LIST):
            duplicate_list = Utils.duplicate_list(value, feedback=True)
            self.assertEqual(
                duplicate_list,
                const.LIST_DUPLICATE_LIST_FEEDBACK[index]
            )

        for index, value in enumerate(const.DICT):
            created_list = Utils.create_list(value, 'id')
            duplicate_list = Utils.duplicate_list(created_list, feedback=True)
            self.assertEqual(
                duplicate_list,
                const.DICT_DUPLICATE_LIST_FEEDBACK[index]
            )
