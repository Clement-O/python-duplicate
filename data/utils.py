

class Utils:

    @staticmethod
    def create_list(obj, key):
        """
        Create a list of all item of a given key
            Ex: obj = [{'id': 1}, {'id': 2}] . key = 'id'
        :return: [1, 2]
        """
        return [value.get(key) for value in obj]

    @staticmethod
    def get_type(item):
        """
        Get the type of the first item
        :return: item_type
        """
        item_type = list
        if isinstance(item, (int, float)):
            item_type = (int, float)
        elif isinstance(item, str):
            item_type = str
        elif isinstance(item, dict):
            item_type = dict
        elif isinstance(item, tuple):
            item_type = tuple
        return item_type

    @staticmethod
    def get_information(obj, item_type):
        """
        Check if all items are of the same type
            if not: raise an TypeError
            if yes: return it and the number of item
        :return:
            [
                {'type': (TYPES), 'nb_item': NUMBER_OF_ITEM},
            ]
        """
        if all(isinstance(x, item_type) for x in obj):
            return {'type': item_type, 'nb_item': len(obj)}
        else:
            raise TypeError(f'An item has a different type than the others')

    @staticmethod
    def duplicate_list(obj, feedback=False):
        """
        Identify every duplicate and return the index of each of them
        :return without feedback:
            [
                {'all_index': [REVERSED_ORDER_INDEXES]}
            ]
        :return with feedback:
            [
                {'all_index': [REVERSED_ORDER_INDEXES]},
                {'value': VALUE, 'index': [INDEX(ES)]},
                {'value': VALUE, 'index': [INDEX(ES)]},
            ]
        """
        all_index = []
        d_list = [{'all_index': all_index}]
        for index, value in enumerate(obj):
            if obj.count(value) >= 2:
                all_index.append(index)
                if feedback:
                    for d in d_list[0:]:
                        if d.get('value') == value:
                            d['index'].append(index)
                            break
                    else:
                        d_list.append({'value': value, 'index': [index]})
        d_list[0]['all_index'] = sorted(all_index, reverse=True)
        return d_list
