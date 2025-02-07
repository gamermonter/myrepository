from time import sleep
print("/"*10, end= "SUPERFÁCIL")

print("/"*10)
print("Olá tudo bem? Bem vindo ao banco SuperFácil")
sleep(1)

casa = float(input("Qual o valor da casa? R$: "))
salario = float(input("Qual o seu salário? R#: "))
anos = int(input("Em quantos anos você deseja pagar? "))

prestacao = casa / anos * 12
porcentagem = (salario/prestacao) * 100

if porcentagem > 30:
    print("Empréstimo de {:.1f} foi negado, sua prestação é maior que 30% do seu salário\nA porcentagem da da prestação: {:.1f}".format(prestacao,porcentagem))

else:
    print("Emprestimo que custa R${:.1f} mensal foi aceito, seu empresimo está em {:.1f}% ".format(prestacao,porcentagem))
