
contador = 0

while True:
    codigo = int(input("Digite o código do brinquedo: "))

    if codigo == 0:
        break

    if codigo == 1040:
        contador += 1

print("Quantidade de carrinhos vendidos:", contador)
