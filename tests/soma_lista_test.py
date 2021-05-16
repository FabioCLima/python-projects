# soma_lista_test.py   

"""An example of a test module in pytest."""

from tests.soma_lista import total

def test_total_empty() -> None:  
    """Testing if a empty list returns 0.0"""  
    
    assert total([]) == 0.0


def test_total_single_item() -> None:    
    """[Total of a single item list should be the first item's value]"""    
    assert total([110.0]) == 110.0

def test_total_many_items() -> None:
    """Summing up many inputs on xs list"""
    assert total([20, 30, -5]) == 45.0