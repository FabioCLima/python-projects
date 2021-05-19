# Script para testar se um número é primo ou não: 3, 5, 7, 11...

n = int(input("Verificar números primos até: "))
mult = 0

for count in range(2, n):
    if (n % count == 0):
        print("Múltiplo de", count)
        mult += 1
if (mult == 0):
    print("É primo")
else:
    print(f"Tem, {mult}, múltiplos acima de 2 e abaixo de {n}")