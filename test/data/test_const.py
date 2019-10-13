"""
Accept LIST of NUMBERS (INT, FLOAT...), STR, DICT, TUPLE
Each item must be identical to the other (str with str, tuple with tuple),
if not an TypeError will be raise
"""

# LIST
LIST = [
    [
        1.5, 2, 3, 3, 4, 5, 6, 3, 1.5, 4
    ],
    [
        "one comma five", "two", "three", "three", "four", "five", "six",
        "three", "one comma five", "four"
    ],
    [
        (1.5, 2), (3, 4), (3, 4), (5, 6), (3, 1.5), (3, 4)
    ],
    [
        [1.5, 2], [3, 4], [3, 4], [5, 6], [3, 1.5], [3, 4]
    ],
    [
        {"id": 1.5, "value": 'value 0'}, {"id": 2}, {"id": 3},
        {"id": 3, "value": 'value 0'}, {"id": 4, "value": 'value 0'}, {"id": 5},
        {"id": 6}, {"id": 3}, {"id": 1.5, "value": 'value 0'},
        {"id": 4, "value": 'value 0'}
    ]
]
# LIST Expected result
LIST_CREATE_UNIQUE_INDEX = [
    {
        "all_index": [9, 8, 7, 3]
    },
    {
        "all_index": [9, 8, 7, 3]
    },
    {
        "all_index": [5, 2]
    },
    {
        "all_index": [5, 2]
    },
    {
        "all_index": [9, 8, 7]
    }
]
LIST_CREATE_UNIQUE_INDEX_FEEDBACK = [
    {
        "all_index": [9, 8, 7, 3], "3": [3, 7], "1.5": [8], "4": [9]
    },
    {
        "all_index": [9, 8, 7, 3], "three": [3, 7], "one comma five": [8],
        "four": [9]
    },
    {
        "all_index": [5, 2], "(3, 4)": [2, 5]
    },
    {
        "all_index": [5, 2], "[3, 4]": [2, 5]
    },
    {
        "all_index": [9, 8, 7], "{'id': 3}": [7],
        "{'id': 1.5, 'value': 'value 0'}": [8],
        "{'id': 4, 'value': 'value 0'}": [9]
    }
]
LIST_CREATE_UNIQUE = [
    [
        1.5, 2, 3, 4, 5, 6
    ],
    [
        'one comma five', 'two', 'three', 'four', 'five', 'six'
    ],
    [
        (1.5, 2), (3, 4), (5, 6), (3, 1.5)
    ],
    [
        [1.5, 2], [3, 4], [5, 6], [3, 1.5]
    ],
    [
        {"id": 1.5, "value": 'value 0'}, {"id": 2}, {"id": 3},
        {"id": 3, "value": 'value 0'}, {"id": 4, "value": 'value 0'}, {"id": 5},
        {"id": 6}
    ]
]
LIST_GET_INDEXES_UNIQUE = [
    {
        "all_index": [1, 5, 6]
    },
    {
        "all_index": [1, 5, 6]
    },
    {
        "all_index": [0, 3, 4]
    },
    {
        "all_index": [0, 3, 4]
    },
    {
        "all_index": [1, 3, 5, 6]
    }
]
LIST_GET_INDEXES_UNIQUE_WITH_FEEDBACK = [
    {
        "all_index": [1, 5, 6], "2": [1], "5": [5], "6": [6]
    },
    {
        "all_index": [1, 5, 6], "two": [1], "five": [5], "six": [6]
    },
    {
        "all_index": [0, 3, 4], "(1.5, 2)": [0], "(5, 6)": [3], "(3, 1.5)": [4]
    },
    {
        "all_index": [0, 3, 4], "[1.5, 2]": [0], "[5, 6]": [3], "[3, 1.5]": [4]
    },
    {
        "all_index": [1, 3, 5, 6], "{'id': 2}": [1],
        "{'id': 3, 'value': 'value 0'}": [3], "{'id': 5}": [5], "{'id': 6}": [6]
    }
]
LIST_GET_UNIQUE = [
    [
        2, 5, 6
    ],
    [
        'two', 'five', 'six'
    ],
    [
        (1.5, 2), (5, 6), (3, 1.5)
    ],
    [
        [1.5, 2], [5, 6], [3, 1.5]
    ],
    [
        {"id": 2}, {"id": 3, "value": 'value 0'}, {"id": 5}, {"id": 6}
    ]
]
LIST_GET_INDEXES_DUPLICATE = [
    {
        "all_index": [0, 2, 3, 4, 7, 8, 9]
    },
    {
        "all_index": [0, 2, 3, 4, 7, 8, 9]
    },
    {
        "all_index": [1, 2, 5]
    },
    {
        "all_index": [1, 2, 5]
    },
    {
        "all_index": [0, 2, 4, 7, 8, 9]
    }
]
LIST_GET_INDEXES_DUPLICATE_WITH_FEEDBACK = [
    {
        "all_index": [0, 2, 3, 4, 7, 8, 9], "1.5": [0, 8], "3": [2, 3, 7],
        "4": [4, 9]
    },
    {
        "all_index": [0, 2, 3, 4, 7, 8, 9], "one comma five": [0, 8],
        "three": [2, 3, 7], "four": [4, 9]
    },
    {
        "all_index": [1, 2, 5], "(3, 4)": [1, 2, 5]
    },
    {
        "all_index": [1, 2, 5], "[3, 4]": [1, 2, 5]
    },
    {
        "all_index": [0, 2, 4, 7, 8, 9],
        "{'id': 1.5, 'value': 'value 0'}": [0, 8], "{'id': 3}": [2, 7],
        "{'id': 4, 'value': 'value 0'}": [4, 9]
    }
]
LIST_GET_DUPLICATE = [
    [
        1.5, 3, 3, 4, 3, 1.5, 4
    ],
    [
        'one comma five', 'three', 'three', 'four', 'three', 'one comma five',
        'four'
    ],
    [
        (3, 4), (3, 4), (3, 4)
    ],
    [
        [3, 4], [3, 4], [3, 4]
    ],
    [
        {"id": 1.5, "value": 'value 0'}, {"id": 3},
        {"id": 4, "value": 'value 0'}, {"id": 3},
        {"id": 1.5, "value": 'value 0'}, {"id": 4, "value": 'value 0'}
    ]
]
# END LIST Expected result

# DICT
DICT = [
    [
        {"id": 1.5, "value": 'value 0'}, {"id": 2, "value": 'value 1'},
        {"id": 3, "value": 'value 2'}, {"id": 3, "value": 'value 3'},
        {"id": 4, "value": 'value 4'}, {"id": 5, "value": 'value 5'},
        {"id": 6, "value": 'value 6'}, {"id": 3, "value": 'value 7'},
        {"id": 1.5, "value": 'value 8'}, {"id": 4, "value": 'value 9'}
    ],
    [
        {"id": [1.5, 2], "value": 'value 0'},
        {"id": [3, 4], "value": 'value 1'}, {"id": [3, 4], "value": 'value 2'},
        {"id": [5, 6], "value": 'value 3'},
        {"id": [3, 1.5], "value": 'value 4'}, {"id": [3, 4], "value": 'value 5'}
    ]
]
# DICT Expected result
DICT_CREATE_UNIQUE_INDEX = [
    {
        "all_index": [9, 8, 7, 3]
    },
    {
        "all_index": [5, 2]
    }
]
DICT_CREATE_UNIQUE_INDEX_WITH_FEEDBACK = [
    {
        "all_index": [9, 8, 7, 3], "3": [3, 7], "1.5": [8], "4": [9]
    },
    {
        "all_index": [5, 2], "[3, 4]": [2, 5]
    }
]
DICT_CREATE_UNIQUE = [
    [
        {"id": 1.5, "value": 'value 0'}, {"id": 2, "value": 'value 1'},
        {"id": 3, "value": 'value 2'}, {"id": 4, "value": 'value 4'},
        {"id": 5, "value": 'value 5'}, {"id": 6, "value": 'value 6'}
    ],
    [
        {"id": [1.5, 2], "value": 'value 0'},
        {"id": [3, 4], "value": 'value 1'}, {"id": [5, 6], "value": 'value 3'},
        {"id": [3, 1.5], "value": 'value 4'}
    ]
]
DICT_GET_INDEXES_UNIQUE = [
    {
        "all_index": [1, 5, 6]
    },
    {
        "all_index": [0, 3, 4]
    }
]
DICT_GET_INDEXES_UNIQUE_WITH_FEEDBACK = [
    {
        "all_index": [1, 5, 6], "2": [1], "5": [5], "6": [6]
    },
    {
        "all_index": [0, 3, 4], "[1.5, 2]": [0], "[5, 6]": [3], "[3, 1.5]": [4],
    }
]
DICT_GET_UNIQUE = [
    [
        {"id": 2, "value": 'value 1'}, {"id": 5, "value": 'value 5'},
        {"id": 6, "value": 'value 6'}
    ],
    [
        {"id": [1.5, 2], "value": 'value 0'},
        {"id": [5, 6], "value": 'value 3'}, {"id": [3, 1.5], "value": 'value 4'}
    ]
]
DICT_GET_INDEXES_DUPLICATE = [
    {
        "all_index": [0, 2, 3, 4, 7, 8, 9]
    },
    {
        "all_index": [1, 2, 5]
    }
]
DICT_GET_INDEXES_DUPLICATE_WITH_FEEDBACK = [
    {
        "all_index": [0, 2, 3, 4, 7, 8, 9], "1.5": [0, 8], "3": [2, 3, 7],
        "4": [4, 9]
    },
    {
        "all_index": [1, 2, 5], "[3, 4]": [1, 2, 5]
    }
]
DICT_GET_DUPLICATE = [
    [
        {"id": 1.5, "value": 'value 0'}, {"id": 3, "value": 'value 2'},
        {"id": 3, "value": 'value 3'}, {"id": 4, "value": 'value 4'},
        {"id": 3, "value": 'value 7'}, {"id": 1.5, "value": 'value 8'},
        {"id": 4, "value": 'value 9'}
    ],
    [
        {"id": [3, 4], "value": 'value 1'}, {"id": [3, 4], "value": 'value 2'},
        {"id": [3, 4], "value": 'value 5'}
    ]
]
# END DICT Expected result

# ERROR LIST & DICT
LIST_ERROR = [
    [
        1.5, 2, 3, "three", 4, 5
    ],
    [
        "one comma five", "two", (3, 3), (4, 5)
    ],
    [
        (1.5, 2), (3, 4), 3, (4, 5)
    ],
    [
        [1.5, 2], {"three": 3}, [3, 4, 5]
    ]
]
DICT_ERROR = [
    [
        {"id": 1.5}, {"id": "one comma five"}
    ],
    [
        {"id": 1.5}, {"id": (1.5, 2, 3, 3, 4, 5)}
    ],
    [
        {"id": {"one comma five": 1.5}}, {"id": [1.5, 2, 3, 3, 4, 5]}
    ]
]
