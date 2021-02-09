from cns11643.lookup import LookupComponent


def test_lookup_component():
    lookup_component = LookupComponent()
    word = '雷'
    component = lookup_component(word=word)
    expected = [454, 301]
    assert component == expected
