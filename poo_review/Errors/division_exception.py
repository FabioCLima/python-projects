def divisao(dividendo, divisor):
    try:
        return dividendo / divisor
    except ZeroDivisionError:
        print("Não existe divisão por zero, tente outro divisor.")
        return 1
    except ValueError:
        print("Entre um número válido!.")
        return 0
    except TypeError:
        print('Não há divisão com string, tente novamente.')
        return 1


print(divisao(10, 0))
print(divisao(10, 'a'))
print(divisao('a', 1))
