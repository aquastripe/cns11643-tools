import pytest

from cns11643.lookup import LookupComponent


@pytest.fixture
def lookup_component():
    return LookupComponent()


def test_lookup_component_1(lookup_component):
    word = '雷'
    components = lookup_component(word=word)
    expected = [454, 301]
    assert components == expected


def test_lookup_component_2(lookup_component):
    word = '永'
    components = lookup_component(word=word)
    expected = [342]
    assert components == expected


# test when the word has multiple component list
def test_lookup_component_3(lookup_component):
    word = '衛'
    components = lookup_component(word=word)
    expected = [127, 151, 119, 111, 19, 10]
    assert components == expected
