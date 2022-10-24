__author__ = 'Wilro - https://github.com/SciWilro'
'''
Usage:
$ pytest test_jar.py
Description:
Tests the Jar() class from the jar.py module
'''

import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(99)
    assert jar.capacity == 99

def test_str():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == '🍪🍪🍪🍪🍪'
    jar.withdraw(5)
    assert str(jar) == ''

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(8)

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    with pytest.raises(ValueError):
        jar.withdraw(8)