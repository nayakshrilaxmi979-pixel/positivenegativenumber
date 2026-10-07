from positive_negative import positiveandnegative


def test_positive():
    assert positiveandnegative(7) == "Positive number"


def test_negative():
    assert positiveandnegative(-7) == "Negative number"

