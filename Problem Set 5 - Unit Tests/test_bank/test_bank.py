__author__ = "Wilro - https://github.com/SciWilro"
import pytest

from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value(" Hello ") == 0


def test_h():
    assert value("Hi") == 20
    assert value("HI") == 20
    assert value("hi") == 20


def test_other():
    assert value("bonjour") == 100
    assert value("asalaam alaikum") == 100
    assert value("konnichiwa") == 100
