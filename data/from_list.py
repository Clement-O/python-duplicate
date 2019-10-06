from copy import deepcopy

# Local import
import data.const as const
from .utils import Utils


class FromList(Utils):

    def __init__(self, lst, key=None):
        Utils.__init__(self, lst)
        self.copied_lst = deepcopy(lst)
        if key:
            self.create_list(key)
        self.get_type()
        self.validate_items()

    def analyze(self, analyze_type, feedback=True):
        """
        Analyze the list to get the items and their indexes
        (depending on the analyze_type)
        :return: {
            "all_index": [INDEX(ES)],
            "VALUE_1": [INDEX(ES)],
            "VALUE_2": [INDEX(ES)],
        }
        """
        if analyze_type == const.ANALYSE_UNIQUE:
            return self.get_indexes(const.INDEX_UNIQUE, feedback)
        if analyze_type == const.ANALYSE_DUPLICATE:
            return self.get_indexes(const.INDEX_DUPLICATE, feedback)
        if analyze_type == const.ANALYSE_CREATE_UNIQUE:
            return self.create_unique_index(feedback)

    def create_unique(self):
        """
        Delete duplicate item to create a list of unique items
        :return: [list]
        """
        indexes = self.create_unique_index()

        for index in indexes['all_index']:
            del self.copied_lst[index]

        return self.copied_lst

    def get_unique(self):
        """
        Get only all unique items
        :return: [list]
        """
        indexes = self.get_indexes(const.INDEX_UNIQUE)

        return [self.copied_lst[index] for index in indexes['all_index']]

    def get_duplicate(self):
        """
        Get only all duplicate items
        :return: [list]
        """
        indexes = self.get_indexes(const.INDEX_DUPLICATE)

        return [self.copied_lst[index] for index in indexes['all_index']]
