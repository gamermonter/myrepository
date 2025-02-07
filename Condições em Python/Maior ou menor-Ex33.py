a = int(input("Escolha um valor: "))
b = int(input("Escolha um outro valor: "))



if a == b:
    print("Ambos são iguais.")
else:
    print("O valor do primeiro número é: ", end="")
    if a > b:
            print("maior") 
    else:
        print("menor")

    print("O valor do segundo número é: ", end="")
    if b > a:
        print("maior")
    else:
        print("menor")

    