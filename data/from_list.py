from copy import deepcopy

# Local import
import data.const as const
from .utils import Utils


class FromList(Utils):

    def __init__(self, obj, key=None):
        Utils.__init__(self, obj)
        self.copied_obj = deepcopy(obj)
        if key:
            self.create_list(key)
        self.get_type()
        self.validate_items()

    def analyse(self, analyse_type, feedback=True):
        if analyse_type == const.ANALYSE_UNIQUE:
            return self.get_indexes(const.INDEX_UNIQUE, feedback)
        if analyse_type == const.ANALYSE_DUPLICATE:
            return self.get_indexes(const.INDEX_DUPLICATE, feedback)
        if analyse_type == const.ANALYSE_CREATE_UNIQUE:
            return self.create_unique_index(feedback)

    def create_unique(self):
        indexes = self.create_unique_index()

        for index in indexes['all_index']:
            del self.copied_obj[index]

        return self.copied_obj

    def get_unique(self):
        # Get only all unique items
        indexes = self.get_indexes(const.INDEX_UNIQUE)

        return [self.copied_obj[index] for index in indexes['all_index']]

    def get_duplicate(self):
        # Get only all duplicate items
        indexes = self.get_indexes(const.INDEX_DUPLICATE)

        return [self.copied_obj[index] for index in indexes['all_index']]
