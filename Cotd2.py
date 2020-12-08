import pytest

def counting(input):

    uppercount = 0
    lowercount = 0
    for letter in input:
        if letter.isupper():
            uppercount += 1
        elif letter.islower():
            lowercount += 1
        else:
            uppercount = uppercount
            lowercount = lowercount
    return uppercount,lowercount

def test_counting():
    assert counting("ThIsHasALOtofcase issues") == (6,17)
    assert counting("") == (0,0)
    assert counting("THISLIKESDGHOISUTHGN") == (20,0)
    assert counting("all lower") == (0,8)

