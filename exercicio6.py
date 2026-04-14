
contador = 0

for i in range(10):
    temp = float(input("Digite a temperatura: "))
    
    if 15 <= temp <= 25:
        contador += 1

print("Quantidade entre 15°C e 25°C:", contador)
