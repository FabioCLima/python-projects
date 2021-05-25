""" Crie um programa simples para simular o lançamento de um dado, que a cada
laço de repetição verifique se o número inserido pelo usuário é igual ao valor
aleatório do lançamento. O programa deve ser repetido indefinidamente até que
o usuário digite 0 ou se o número digitado estiver fora do intervalo [1,6].
Ao final mostre o número de acertos e a quantidade de jogadas. """


from random import randint


def dice_simulator():
    
    escolha = 1
    acertos = 0
    jogadas = 0
    
    while escolha != 0:
        bot = randint(1, 6)
        escolha = int(input("Digite 0 para sair ou escolha um número entre 1-6:   "))
        if escolha in [1, 2, 3, 4, 5, 6]:
            jogadas += 1
            if escolha == bot:
                print("Você acertou!")
                acertos += 1
            else:
                print("Você errou!")
        else:
            print('Escolha inválida. O jogo encerrou!')
            break
    print(f"Número de partidas jogadas: {jogadas}")
    print(f"Número de acertos: {acertos}")


if __name__ == "__main__":
    dice_simulator()
