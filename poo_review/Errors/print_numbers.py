def print_even_numbers(lista: list):
    try:
        for n in lista:
            if n % 2 == 0:
                print(n)
    except ValueError:
        print("Digite um número válido")
    finally:
        print("Não use strings na lista")


lista = list(range(0, 21))
lista.append(a)
print_even_numbers(lista)
