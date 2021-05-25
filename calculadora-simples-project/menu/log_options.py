from utils.logaritmos import log_N, log10_N, log2_N


OPERATIONS_CHOICES = """
    Enter:
    - '1'     log_N
    - '2'    log2_N
    - '3'   log10_N

Operações disponíveis   """


def menu_log_operations():

    print("Escolha uma operação para cálculo de log: 'log', 'log2' e 'log10'")
    option = input(OPERATIONS_CHOICES)

    if option == "1":
        resultado = log_N()
        print(f"{resultado}")
    elif option == '3':
        resultado = log10_N()
        print(f"{resultado}")
    elif option == '2':
        resultado = log2_N()
        print(f"{resultado}")
    else:
        print("Operação indisponível, tente novamente.")
