# soma_lista.py     

from typing import List

def total(xs: List[float]) -> float:   
    """[Total returns the sum of xs.]

    Args:
        xs (List[float]): [list of float numbers]

    Returns:
        float: [the sum of the float numbers in input list]
    """
    result: float = 0.0
    # For each x float in xs, add to result
    for x in xs:   
        result += x
    return result

