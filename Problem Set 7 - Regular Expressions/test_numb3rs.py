__author__ = 'Wilro - https://github.com/SciWilro'

import pytest

from numb3rs import validate
def test_validation_valid():
    assert validate("123.55.5.123") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True

def test_validation_invalid():
    assert validate("256.255.255.255") == False
    assert validate("123.55.5.300") == False
    assert validate("cat") == False