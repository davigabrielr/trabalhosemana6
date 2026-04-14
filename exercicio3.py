
soma = 0
menos_30 = 0
entre_30_60 = 0

for i in range(7):
    tempo = float(input("Digite o tempo do corredor: "))
    
    soma += tempo
    
    if tempo < 30:
        menos_30 += 1
    
    if 30 <= tempo <= 60:
        entre_30_60 += 1

media = soma / 7
porcentagem = (entre_30_60 / 7) * 100

print("Tempo médio:", media)
print("Corredores abaixo de 30 min:", menos_30)
print("Porcentagem entre 30 e 60 min:", porcentagem, "%")
