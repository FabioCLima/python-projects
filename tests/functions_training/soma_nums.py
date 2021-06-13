# soma_nums.py
"""[Elabore uma função que retorne a soma de 2 números]"""

def soma(x: float, y: float) -> float:
    """[Retorna a soma de dois números]

    Args:
        x (float): [número]
        y (float): [número]

    Returns:
        float: [soma dos 2 números informados]
    """

    try:
        return x + y
    except TypeError:
        print("Parâmetro inválido. Uma exceção ocorreu.")
