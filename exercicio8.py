
caixa = float(input("Digite o valor inicial em caixa: "))

while True:
    print("\n1 - Realizar venda")
    print("2 - Retirar dinheiro")
    print("3 - Mostrar dinheiro em caixa")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        valor = float(input("Valor da venda: "))
        caixa += valor

    elif opcao == 2:
        valor = float(input("Valor a retirar: "))
        
        if valor <= caixa:
            caixa -= valor
    
        else:
            print("Saldo insuficiente!")

    elif opcao == 3:
        print("Dinheiro em caixa:", caixa)

    elif opcao == 4:
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
