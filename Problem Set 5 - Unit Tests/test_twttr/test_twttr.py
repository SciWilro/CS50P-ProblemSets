# __author__ = "Wilro - https://github.com/SciWilro"

# Was tricky to work out what to do here
# But the results of check50 gives the scenarios to check for
# NB submit50 and check50 don't use YOUR twttr.py file
# See the commented lines

import pytest
from twttr import shorten


def test_shorten():
    # catches twttr.py without vowel replacement
    assert shorten("testING") == "tstNG"
    # catches twttr.py without capitalized vowel replacement
    assert shorten("TESTING") == "TSTNG"
    # twttr.py without lowercase vowel replacement
    assert shorten("testing") == "tstng"
    # catches twttr.py omitting numbers
    assert shorten("0Testing") == "0Tstng"
    # catches twttr.py printing in uppercase
    assert shorten("testing") == "tstng"
    # catches twttr.py omitting punctuation
    assert shorten("!testing!") == "!tstng!"

    with pytest.raises(TypeError):
        shorten(5)
