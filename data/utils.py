# Local import
from .const import DUPLICATE, UNIQUE


class Utils:

    def __init__(self, lst):
        self.indexes = {}
        self.lst = lst
        self.item_type = list

    def create_list(self, key):
        """
        Create a list of all item of a given key
            Ex: obj = [{'id': 1}, {'id': 2}] . key = 'id'

        :return: [1, 2]
        """
        self.lst = [value.get(key) for value in self.lst]

    def get_type(self):
        """
        Get the type of the first item

        :return: item_type
        """
        item = self.lst[0]
        if isinstance(item, (int, float)):
            self.item_type = (int, float)
        elif isinstance(item, str):
            self.item_type = str
        elif isinstance(item, dict):
            self.item_type = dict
        elif isinstance(item, tuple):
            self.item_type = tuple

    def validate_items(self):
        """
        Check if all items are of the same type

        :return:
            if not: raise an TypeError
            if yes: nothing
        """
        if not all(isinstance(x, self.item_type) for x in self.lst):
            raise TypeError(f'An item has a different type than the others')

    def create_update_feedback(self, index, value, feedback):
        """
        Create or update the 'self.indexes' dict to provide feedback

        :return: { VALUE: [INDEX(ES)] }
        """
        if feedback:
            str_value = str(value)
            if self.indexes.get(str_value):
                self.indexes[str_value].append(index)
            else:
                self.indexes.update({str_value: [index]})

    def get_indexes(self, index_type, feedback=False):
        """
        Identify unique or duplicate item and return the index of each of them

        :return:
            without feedback:
                {
                    "all_index": [INDEX(ES)]
                }
            with feedback:
                {
                    "all_index": [INDEX(ES)],
                    VALUE_X: [INDEX(ES)],
                    VALUE_Y: [INDEX(ES)],
                }
        """
        indexes = []
        for index, value in enumerate(self.lst):
            if index_type == DUPLICATE and self.lst.count(value) >= 2:
                self.create_update_feedback(index, value, feedback)
                indexes.append(index)
            if index_type == UNIQUE and self.lst.count(value) == 1:
                self.create_update_feedback(index, value, feedback)
                indexes.append(index)
        self.indexes['all_index'] = indexes
        return self.indexes

    def create_unique_index(self, feedback=False):
        """
        Identify duplicated item and return the index of each of them except for
        the first one (in order to create a list of unique item)

        :return:
            without feedback:
                {
                    "all_index": [REVERSED_ORDER_INDEX(ES)]
                }
            with feedback:
                {
                    "all_index": [REVERSED_ORDER_INDEX(ES)],
                    VALUE_X: [INDEX(ES)],
                    VALUE_Y: [INDEX(ES)],
                }
        """
        seen_value = []
        seen_index = []
        for index, value in enumerate(self.lst):
            if self.lst.count(value) >= 2:
                if value not in seen_value:
                    seen_value.append(value)
                else:
                    seen_index.append(index)
                    self.create_update_feedback(index, value, feedback)
        self.indexes['all_index'] = sorted(seen_index, reverse=True)
        return self.indexes
