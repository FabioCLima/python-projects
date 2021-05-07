# join_list_strings_test.py

from tests.join_list_strings import join

def test_join_use_case() -> None:  
    """This will test a use case, give a valid list and delimiter."""  
    assert join([1, 2, 3], "-") == "1-2-3"


def test_join_edge_single_item() -> None:     
    assert join([1], ", ") == "1"



def test_join_empty_delimeter()-> None:
    """This will test a empty delimiter"""
    
    assert join([1, 2, 3], "") == "123"