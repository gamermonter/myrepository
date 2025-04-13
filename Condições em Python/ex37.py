while True:
    x = input("Digite um número: ")

    print("Você quer converter para?: ")
    print("1 - Binário")
    print("2 - Octal") 
    print("3 - Hexadecimal")
    opcao = int(input("Escolha uma das opções: "))


    if opcao == 1:
        print("O número {} em binário é {}".format(x, bin(int(x))[2:]))
        break
    elif opcao == 2:
        print("O número {} em octal é {}".format(x, oct(int(x))[2:]))
        break
    elif opcao == 3:
        print("O número {} em hexadecimal é {}".format(x, hex(int(x))[2:]))
        break
    else:
        print("Não temos essa opção tente novamente")

