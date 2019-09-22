# Accept LIST of NUMBERS (INT, FLOAT...), STR, DICT, TUPLE
# Each item must be identical to the other (str with str, tuple with tuple)
LIST = [
    [1.5, 2, 3, 3, 4, 5],
    ['one comma five', 'two', 'three', 'three', 'four', 'five'],
    [(1.5, 2), (3, 4), (3, 4), (5, 5)],
    [[1.5, 2], [3, 4], [3, 4], [5, 5]],
    [
        {'id': 1.5}, {'id': 2}, {'id': 3},
        {'id': 3}, {'id': 4}, {'id': 5},
    ],
]
# Expected result
LIST_GET_INFORMATION = [
    {'type': (int, float), 'nb_item': 6},
    {'type': str, 'nb_item': 6},
    {'type': tuple, 'nb_item': 4},
    {'type': list, 'nb_item': 4},
    {'type': dict, 'nb_item': 6},
]
LIST_DUPLICATE_LIST = [
    [{'all_index': [3, 2]}],
    [{'all_index': [3, 2]}],
    [{'all_index': [2, 1]}],
    [{'all_index': [2, 1]}],
    [{'all_index': [3, 2]}],
]
LIST_DUPLICATE_LIST_FEEDBACK = [
    [{'all_index': [3, 2]}, {'index': [2, 3], 'value': 3}],
    [{'all_index': [3, 2]}, {'index': [2, 3], 'value': 'three'}],
    [{'all_index': [2, 1]}, {'index': [1, 2], 'value': (3, 4)}],
    [{'all_index': [2, 1]}, {'index': [1, 2], 'value': [3, 4]}],
    [{'all_index': [3, 2]}, {'index': [2, 3], 'value': {'id': 3}}],
]

DICT = [
    [
        {'id': 1.5}, {'id': 2},
        {'id': 3}, {'id': 3},
        {'id': 4}, {'id': 5},
    ],
    [
        {'id': [1.5]}, {'id': [2]},
        {'id': [3]}, {'id': [3]},
        {'id': [4]}, {'id': [5]},
    ],
]
# Expected result
DICT_GET_INFORMATION = [
    {'type': (int, float), 'nb_item': 6},
    {'type': list, 'nb_item': 6},
]
DICT_DUPLICATE_LIST = [
    [{'all_index': [3, 2]}],
    [{'all_index': [3, 2]}],
]
DICT_DUPLICATE_LIST_FEEDBACK = [
    [{'all_index': [3, 2]}, {'index': [2, 3], 'value': 3}],
    [{'all_index': [3, 2]}, {'index': [2, 3], 'value': [3]}],
]


# Any mix of item result in an TypeError (str with nb, dict with tuple, etc..)
LIST_ERROR = [
    [1.5, 2, 3, 'three', 4, 5],
    [(1.5, 2), (3, 4), 3, (4, 5)],
    [[1.5, 2], {'three': 3}, [3, 4, 5]],
]
DICT_ERROR = [
    [{'id': 1.5}, {'id': 'one comma five'}],
    [{'id': 1.5}, {'id': (1.5, 2, 3, 3, 4, 5)}],
    [{'id': {'one comma five': 1.5}}, {'id': [1.5, 2, 3, 3, 4, 5]}],
]
