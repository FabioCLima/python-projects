"""Operações aritméticas"""


def soma():
    """[Função para somar dois números]

    Returns:
        [float]: [a soma aritmética de 2 números]
    """
    num1 = input("Digite o num1.  ")
    num2 = input("Digite o num2.  ")
    try:
        x = float(num1)
        y = float(num2)
        resultado = x + y
        return resultado

    except ValueError:
        return "Operação não permitida. Digite um número válido."


def subtração():
    """[Função para fazer a subtração entre dois números]

    Returns:
        [float]: [a diferença aritmética de 2 números]
    """
    num1 = input("Digite o num1.  ")
    num2 = input("Digite o num2.  ")
    try:
        x = float(num1)
        y = float(num2)
        resultado = x - y
        return resultado

    except ValueError:
        return "Operação não permitida. Digite um número válido."


def multiplicação():
    """[Função para fazer a multiplicação entre dois números]

    Returns:
        [float]: [a diferença aritmética de 2 números]
    """
    num1 = input("Digite o num1.  ")
    num2 = input("Digite o num2.  ")
    try:
        x = float(num1)
        y = float(num2)
        resultado = x * y
        return resultado

    except ValueError:
        return "Operação não permitida. Digite um número válido."


def divisão():
    """[Função para calcular a divisão entre 2 números válidos.]

    Returns:
        [float]: [o resultado da divisão aritmética entre dois números.]
    """    
    num1 = input("Digite o num1.  ")
    num2 = input("Digite o num2.  ")
    try:
        x = float(num1)
        y = float(num2)
        return f"{x}/{y} = {x/y}"

    except ValueError:
        return "Operação não permitida. Digite um número(s) válido(s)."

    except ZeroDivisionError:
        return f"O denominador y = {y},deve ser um número diferente de zero."


def potenciação():
    num1 = input('Digite o número da base. ')
    num2 = input('Digite o número para o expoente. \n')
    try:
        base = int(num1)
        expoente = int(num2)
        return f"{base} elevado a {expoente} = {base**expoente}"
    except ValueError:
        print("A sua entrada é inválida. Usando valor padrão pra expressão 0")
        return 0
