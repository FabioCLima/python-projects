
     

        if option == '+':
            print('\nVamos executar a soma entre 2 números:')
            print(f'A soma dos números informados é: {soma(num1, num2)}\n')
        elif option == '-':
            print('\nVamos executar a subtração entre 2 números:')
            print(f'A soma dos números informados é: {diff(num1, num2)}\n')
        elif option == '*':
            print('\nVamos executar a multiplicação entre 2 números:')
            print(f'A soma dos números informados é: {produto(num1, num2)}\n')
        elif option == '/':
            print('\nVamos executar a multiplicação entre 2 números:')
            print(f'A soma dos números informados é: {division(num1, num2)}\n')
        else:
            print("Opção inválida !")
            print("saindo !!!")
    else:
        print("Escolha uma operação aritimética válida")
