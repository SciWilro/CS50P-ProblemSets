__author__ = 'Wilro - https://github.com/SciWilro'
'''
Usage:
$ pytest test_um.py

Description:
Tests the count(s) function in the um.py file
'''

import pytest
from um import count

def test_count_valid():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, I um....") == 2
    assert count("Um?") == 1
    
def test_count_invalid():
    assert count("Thanks for the album, and the umbrella.") == 0