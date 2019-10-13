# python-duplicate 
[![Build Status](https://travis-ci.com/Clement-O/python-duplicate.svg?branch=master)](https://travis-ci.com/Clement-O/python-duplicate) 
[![Coverage Status](https://coveralls.io/repos/github/Clement-O/python-duplicate/badge.svg?branch=master)](https://coveralls.io/github/Clement-O/python-duplicate?branch=master)

The python-duplicate repo (soon to be library) intend to find and deal with duplicate.
Depending on what you need, it can:
- Find and return the unique or duplicate items* of a list
- Create a new list of unique items* from a list
- Find and return the indexes of said items* (act as a feedback)

*items can be a list, tuple, dict, number or string

## Upcoming improvements
Dealing with duplicate on limited type of list is just the begining.
In the future I intend to add support for:
- Database (starting with postgreSQL & mySQL)
- JSON
- Other type of item for list (Object class for example)

Alternatively, you can look at the project tab of this repo.

## Doc
Available at : [TODO](add_link)

## Examples
##### Import the class
```python
from data.from_list import FromList
```
##### Create unique items from a list of number
```python
lst = [1.5, 2, 3, 3, 4, 5, 6, 3, 1.5, 4]

from_list = FromList(lst)
returned_lst = from_list.create_unique()

# >>> [1.5, 2, 3, 4, 5, 6]
```
##### Get unique items from a list of tuple
```python
lst = [(1.5, 2), (3, 4), (3, 4), (5, 6), (3, 1.5), (3, 4)]

from_list = FromList(lst)
returned_lst = from_list.get_unique()

# >>> [(1.5, 2), (5, 6), (3, 1.5)]
```
##### Get duplicate items from a list of dict (on the key "id" only)
```python
lst = [
    {"id": [1.5, 2], "value": 'value 0'}, {"id": [3, 4], "value": 'value 1'}, 
    {"id": [3, 4], "value": 'value 2'}, {"id": [5, 6], "value": 'value 3'},
    {"id": [3, 1.5], "value": 'value 5'}, {"id": [3, 4], "value": 'value 6'}
]

from_list = FromList(lst, key='id')
returned_lst = from_list.get_duplicate()

# >>> [
#   {"id": [3, 4], "value": 'value 1'}, 
#   {"id": [3, 4], "value": 'value 2'},
#   {"id": [3, 4], "value": 'value 5'}
# ]
```
##### Get feedback of unique items of a list of string
```python
from data.const import UNIQUE

lst = [
    "one comma five", "two", "three", "three", "four", "five", "six",
    "three", "one comma five", "four"
]

from_list = FromList(lst)
returned_lst = from_list.analyze(UNIQUE)

# >>> {
#   "all_index": [1, 5, 6], "two": [1], "five": [5], "six": [6]
# }
```
