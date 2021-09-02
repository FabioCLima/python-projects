from typing import List


def divide(dividendo: float, divisor: int) -> float:
    if divisor == 0:
        raise ZeroDivisionError("Divisor não pode ser zero")

    return dividendo / divisor


notas: List = []

print("Seja bem vindo ao programa de cálculo da média: ")

try:
    media = divide(sum(notas), len(notas))
except ZeroDivisionError:
    print("Não há notas ainda na sua lista")
else:  # executa se não houver erros
    print(f"A média das notas inputadas é {media}")
finally:  # executa sempre
    print("Fim da execução do cálculo das médias !.")
