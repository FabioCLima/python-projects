# test_divide_integers.py

from divide_integers import divide

def test_case1():
    assert 5 == divide(10, 2) # calls the function we want to test


def test_case2():
    assert 'Not defined' == divide(10, 0)


def test_case3():
    assert 3 == divide(10, 3)
    

def test_case4():     
    assert "Numerator/denominator value is None" == divide(None, 3)