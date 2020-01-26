.. _examples:


Examples
========

Data
----

Import the class

.. code:: python

    from pyduplicate import FromList

Create unique items from a list of number

.. code:: python

    lst = [1.5, 2, 3, 3, 4, 5, 6, 3, 1.5, 4]

    from_list = FromList(lst)
    returned_lst = from_list.create_unique()

    # It will return:
    # [1.5, 2, 3, 4, 5, 6]

Get unique items from a list of tuple

.. code:: python

    lst = [(1.5, 2), (3, 4), (3, 4), (5, 6), (3, 1.5), (3, 4)]

    from_list = FromList(lst)
    returned_lst = from_list.get_unique()

    # It will return:
    # [(1.5, 2), (5, 6), (3, 1.5)]

Get duplicate items from a list of dict (on the key "id" only)

.. code:: python

    lst = [
        {"id": [1.5, 2], "value": 'value 0'}, {"id": [3, 4], "value": 'value 1'},
        {"id": [3, 4], "value": 'value 2'}, {"id": [5, 6], "value": 'value 3'},
        {"id": [3, 1.5], "value": 'value 5'}, {"id": [3, 4], "value": 'value 6'}
    ]

    from_list = FromList(lst, key='id')
    returned_lst = from_list.get_duplicate()

    # It will return:
    # [
    #   {"id": [3, 4], "value": 'value 1'},
    #   {"id": [3, 4], "value": 'value 2'},
    #   {"id": [3, 4], "value": 'value 5'}
    # ]

Get feedback of unique items of a list of string

.. code:: python

    lst = [
        "one comma five", "two", "three", "three", "four", "five", "six",
        "three", "one comma five", "four"
    ]

    from_list = FromList(lst)
    returned_lst = from_list.analyze('unique')  # or 'duplicate'

    # It will return:
    # { "all_index": [1, 5, 6], "two": [1], "five": [5], "six": [6] }

Database
--------

All examples below will use this table

.. code:: sql

    CREATE TABLE `address` (
        `id` SMALLINT PRIMARY KEY,
        `complete_address` VARCHAR (255) NOT NULL,
        `country_id` SMALLINT REFERENCES country(id),
        `resident_id` SMALLINT REFERENCES resident(id)
    );

Import the class and define dictionary to connect on the Database
It use the same naming convention as Django, so you can directly pass the Django conf dict
(All example are done with MySQL, but it's exactly the same with PostgreSQL)

.. code:: python

    from pyduplicate import FromMySQL  # or FromPSQL for Postgres

    INFO_DICT = {
        'HOST': "MYSQL_HOSTNAME",
        'DATABASE': "MYSQL_DATABASE",
        'USER': "MYSQL_USER",
        'PASSWORD': "MYSQL_PASSWORD",
        'PORT': int("MYSQL_PORT"),
    }

Get row or primary key of duplicate column

.. code:: python

    # First param is the connection dict, second the table and third the column on which to search
    from_mysql = FromMySQL(INFO_DICT, 'address', 'complete_address')

    result = self.from_mysql.select_duplicate(rows_list=True)
    # It will return:
    # (
    #   (2, '3 street test', 0, 2),
    #   (4, '5 street test', 1, 4),
    #   (5, '5 street test', 0, 3),
    #   (7, '3 street test', 0, 0)
    # )

    result = self.from_mysql.select_duplicate()
    # It will return:
    # [2, 4, 5, 7]

Get row or primary key of unique column

.. code:: python

    # First param is the connection dict, second the table and third the column on which to search
    from_mysql = FromMySQL(INFO_DICT, 'address', 'complete_address')

    result = self.from_mysql.select_unique(rows_list=True)
    # It will return:
    # (
    #   (0, '1 street test', 0, 0),
    #   (1, '2 street test', 1, 1),
    #   (3, '4 street test', 0, 3),
    #   (6, '6 street test', 0, 4)
    # )

    result = self.from_mysql.select_unique()
    # It will return:
    # [0, 1, 3, 6]
