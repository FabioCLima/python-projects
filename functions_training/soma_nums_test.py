# soma_2_nums_test.py
"""[Testes unitários da função que retorna a soma de 2 números]"""

import pytest
from functions_training.soma_nums import soma


def test_soma_usecase() -> None:
    """Testar o retorno de 2 + (-3)"""
    assert soma(2, -3) == -1


def test_soma_usecase2() -> None:    
    """[Testar o retorno de -2 + (-2)]"""
    assert soma(-2, -2) == -4


@pytest.mark.parametrize("x, y, expected", [(3, 5, 8)])
def test_soma_parametrização_usecases(x, y, expected):
    assert soma(x, y) == expected


# Podemos definir uma função para pegar a lista de inputs e outputs
def get_soma_test_data():
    return[(-2, -2,-4), (-1, 5,4), (3, -5,-2), (0, 5, 5)]


@pytest.mark.parametrize("x, y, expected", get_soma_test_data())
def test_soma_parametrização_usecases_list_data(x, y, expected):
    assert soma(x, y) == expected


#! pytest.fixture

@pytest.fixture
def get_soma_test_data():
    return[(-2, -2, -4), (-1, 5, 4), (3, -5, -2), (0, 5, 5)]


def test_soma_fixture(get_soma_test_data):   
    for data in get_soma_test_data:    
        x = data[0]
        y = data[1]
        expected = data[2]
        assert soma(x, y) == expected


@pytest.fixture(scope='session')
def get_soma_test_data2():
    return [(3, 5, 8), (-2, -2, -4), (-1, 5, 4), (3, -5, -2), (0, 5, 5)]


@pytest.fixture(autouse=True)  #make every test in your suite use it by default
def setup_and_teardown():
    print('\nFetching data from db')
    yield
    print('\nSaving test run data in db')


def test_soma_fixture_use(get_soma_test_data2):
    for data in get_soma_test_data2:
        num1 = data[0]
        num2 = data[1]
        expected = data[2]
        assert soma(num1, num2) == expected



@pytest.mark.xfail
def test_soma_edge_case():
    assert soma('a', 'a') == 'aa'

def test_soma_edge_case2():
    assert soma('a', 2.0) == "a" + 2.0