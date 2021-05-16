import random
import string

# #* random.randint, um número inteiro aleatório entre os limites fornecidos
# numeros_inteiro = random.randint(1, 7)
# inteiro  = random.randrange(1,10,2)
# print(f'{inteiro}')

# #* random.uniforme - número flutuante entre os limites fornecidos
# flutuante = random.uniform(1, 7)
# flutuante2 = random.random()
# print(f"{flutuante2}")

# lista = ['casa1', 'Fabio', 'Europa', 'mergulho']

# sorteio = random.choice(lista)
# sorteio2 = random.choices(lista, k = 2)
# sorteio3 = random.sample(lista, k = 2)

#! Gerar senha aleatória
letras = string.ascii_letters
digitos = string.digits
caracteres = "!@#$%&*._-"
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k = 15))
print(senha)



