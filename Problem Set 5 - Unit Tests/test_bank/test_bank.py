__author__ = "Wilro - https://github.com/SciWilro"

import pytest

from bank import value


# test_bank catches bank.py with incorrect values
def test_values():
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("bonjour") == 100


# test_bank catches bank.py without case-insensitivity
def test_case():
    assert value("HELLO") == 0
    assert value("Hi") == 20
    assert value("hi") == 20


# test_bank catches bank.py not allowing for entire phrase
def test_other():
    assert value("asalaam alaikum") == 100
    assert value("What's Up My Dude") == 100
