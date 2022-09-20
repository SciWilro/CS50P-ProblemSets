import pytest

from twttr import shorten


def test_lower():
    assert shorten("testing") == "tstng"


def test_Upper():
    assert shorten("TESTING") == "TSTNG"


def test_spaces():
    assert shorten(" TESTING ") == "TSTNG"


def test_var_type():
    with pytest.raises(TypeError):
        shorten(5)
