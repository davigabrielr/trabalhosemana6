
a = 0
b = 0
c = 0

for i in range(10):
    voto = input("Digite A (Expresso), B (Cappuccino) ou C (Chá): ").upper()
    
    if voto == "A":
        a += 1
    elif voto == "B":
        b += 1
    elif voto == "C":
        c += 1

porc_a = (a / 10) * 100
porc_b = (b / 10) * 100
porc_c = (c / 10) * 100

print("Expresso:", a, "votos -", porc_a, "%")
print("Cappuccino:", b, "votos -", porc_b, "%")
print("Chá:", c, "votos -", porc_c, "%")
