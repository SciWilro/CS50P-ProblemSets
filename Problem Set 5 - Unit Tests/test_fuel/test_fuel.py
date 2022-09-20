__author__ = "Wilro - https://github.com/SciWilro"
import pytest

from fuel import convert, gauge


def test_convert():

    # catches fuel.py not raising ZeroDivisionError in convert
    # catches fuel.py returning incorrect ints in convert
    # catches fuel.py not raising ValueError in convert
    assert convert("1/2") == 50
    with pytest.raises(ValueError):
        convert("1/A")
        convert("2/1")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")


def test_gauge():
    # test_fuel catches fuel.py not labeling 1% as E in gauge
    # test_fuel catches fuel.py not printing % in gauge
    # test_fuel catches fuel.py not labeling 99% as F in gauge
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
