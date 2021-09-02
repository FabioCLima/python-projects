''' Calculadora
Elabore uma calculadora simples que efetue as operações básicas e acrescente
algumas funcionalidades oriundas de uma calculadora científica. '''

from menu.aritmetica_options import menu_aritmetica_operations
from menu.log_options import menu_log_operations
from menu.trigo_options import menu_trig_operations


USER_CHOICE = """
Enter:
- 'a' Operações Aritméticas
- 'l' Funções Logaritmicas
- 't' Funções Trigonométricas
- 'q' sair

Your choice  """

operations = {
    "a": menu_aritmetica_operations,
    "l": menu_log_operations,
    "t": menu_trig_operations
    }


def menu():

    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in operations:
            selected_function = operations[user_input]
            selected_function()
        else:
            print("Opção inválida. Por favor tente novamente.")

        user_input = input(USER_CHOICE)


menu()
