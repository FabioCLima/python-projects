from utils.aritimetica import soma, subtração, multiplicação
from utils.aritimetica import divisão, potenciação


OPERATIONS_CHOICES = """
    Enter:
    - '+' Soma
    - '-' Subtração
    - '*' Multiplicação
    - '/' Divisão
    - '**'Potenciação

Operações disponíveis   """


def menu_aritmetica_operations():

    basic_operations = {
                        "+": soma,
                        "-": subtração,
                        "*": multiplicação,
                        "/": divisão,
                        "**": potenciação}

    print("Escolha uma operação de aritmética básica")
    option = input(OPERATIONS_CHOICES)

    if option in basic_operations:
        select_function = basic_operations[option]
        resultado = select_function()
        print(f"{resultado}")
    else:
        print("Operação indisponível, tente novamente.")
