__author__ = 'Wilro - https://github.com/SciWilro'
'''
Usage:
$ pytest test_response.py
Description:
Tests the check_email() function from the response.py module
'''

import pytest
from response import check_email

def test_check_email():
    assert check_email("malan@harvard.edu") == "Valid"
    assert check_email("mr.wilro@gmail.com") == "Valid"
    assert check_email("malan@@@harvard.edu") == "Invalid"
    assert check_email("malan@harvard..edu") == "Invalid"

