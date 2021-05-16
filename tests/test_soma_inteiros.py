# test_soma_inteiros.py

import pytest
from soma_inteiros import soma

def test_case1():     
    assert soma(1, 2) == 3
    
    
def test_case2():      
    #! testing the output should be as integer as well
    assert isinstance(soma(1, 2), int)

@pytest.mark.parametrize("x, y, expected", [(3, 5, 8)])
def test_cases(x, y, expected):    
    assert soma(x, y) == expected
    

@pytest.mark.parametrize("x, y, expected", [(3, 6, 9), (-1,5,4), (3,-5,-2), (0,5,5)])
def test_cases2(x, y, expected):    
    assert soma(x, y) == expected


def get_soma_test_data():     
    return [(3,3,6), (-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)]


@pytest.mark.parametrize("x, y, expected", get_soma_test_data())
def test_cases3(x, y, expected):    
    assert soma(x, y) == expected
    

@pytest.fixture
def get_test_soma_data():     
    return [(3,3,6), (-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)]

def test_soma(get_test_soma_data):     
    for data in get_test_soma_data:     
        x = data[0]
        y = data[1]
        expected = data[2]
        assert soma(x, y) ==  expected