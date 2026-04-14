
soma_salarios = 0
mais_novo = 999
mais_velho = 0

atacantes_ate_10000 = 0
qtd_atacantes = 0
qtd_defensores = 0

for i in range(10):
    idade = int(input("Idade: "))
    posicao = input("Posição (A/D): ").upper()
    salario = float(input("Salário: "))
    
    soma_salarios += salario

    if idade < mais_novo:
        mais_novo = idade

    if idade > mais_velho:
        mais_velho = idade

    if posicao == "A":
        qtd_atacantes += 1
    elif posicao == "D":
        qtd_defensores += 1

    if posicao == "A" and salario <= 10000:
        atacantes_ate_10000 += 1

media = soma_salarios / 10

print("Média dos salários:", media)
print("Mais novo:", mais_novo)
print("Mais velho:", mais_velho)
print("Atacantes com salário até 10.000:", atacantes_ate_10000)
print("Quantidade de atacantes:", qtd_atacantes)
print("Quantidade de defensores:", qtd_defensores)
