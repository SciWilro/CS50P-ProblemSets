__author__ = 'Wilro - https://github.com/SciWilro'
'''
Usage:
$ pytest test_seasons.py
Description:
Tests the get_birthday() function from the seasons.py module
'''

import pytest
import datetime
from seasons import get_birthday

def test_get_birthday():
    assert get_birthday('1991-07-02') == datetime.date(1991, 7, 2)
    assert get_birthday('2000-01-01') == datetime.date(2000, 1, 1)
