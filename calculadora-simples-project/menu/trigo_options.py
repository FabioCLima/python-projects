from utils.trigonometria import seno, cosseno, tangente

OPERATIONS_CHOICES = """
    Enter:
    - '1'  seno
    - '2'  cosseno
    - '3'  tangente

Operações disponíveis   """


def menu_trig_operations():
    print("Escolha uma operação para cálculo trigonométrico: 'seno', 'cosseno' e 'tangente'")
    option = input(OPERATIONS_CHOICES)
    n = input("Digite um número: \n")
    if option == "1":
        resultado = seno(n)
        print(f"{resultado}")
    elif option == '2':
        resultado = cosseno(n)
        print(f"{resultado}")
    elif option == '3':
        resultado = tangente(n)
        print(f"{resultado}")
    else:
        print("Operação indisponível, tente novamente.")
