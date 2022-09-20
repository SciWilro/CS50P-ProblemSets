__author__ = "Wilro - https://github.com/SciWilro"

import pytest

from plates import is_valid


def test_alphabetical_start():
    # test_plates catches plates.py without beginning alphabetical checks
    assert is_valid("AAA222") == True
    assert is_valid("A22222") == False
    assert is_valid("222222") == False


def test_length():
    # test_plates catches plates.py without length checks
    assert is_valid("A") == False
    assert is_valid("AAAAAAA98") == False


def test_number_placement():
    # test_plates catches plates.py without checks for number placement
    assert is_valid("AAA22A") == False


def test_zero_placement():
    # test_plates catches plates.py without checks for zero placement
    assert is_valid("AAA022") == False


def test_alphanumeric():
    # test_plates catches plates.py without checks for alphanumeric characters
    assert is_valid("YO..OY") == False
