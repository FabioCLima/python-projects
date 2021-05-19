# verificar se um número dado é primo
from math import sqrt


def verificar_primo(n):
    raiz = int(sqrt(n))
    for number in range(2, n):
        if n % number == 0:
            return False
    return True


numero = int(input("Digite um número:  "))
if verificar_primo(numero):
    print(f"O número {numero} é primo")
else:
    print(f"O número {numero} NÃO é primo")
