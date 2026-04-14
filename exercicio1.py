
ingressos_disponiveis = 100

while True:
    print("\n1 - Vender ingresso")
    print("2 - Adicionar ingressos extras")
    print("3 - Mostrar ingressos disponíveis")
    print("4 - Encerrar")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 3:
        print("Ingressos disponíveis:", ingressos_disponiveis)

    elif opcao == 1:
        if ingressos_disponiveis > 0:
            ingressos_disponiveis -= 1
            print("Ingresso vendido!")
        else:
            print("Estádio lotado!")

    elif opcao == 2:
        extras = int(input("Quantos ingressos deseja adicionar? "))
        ingressos_disponiveis += extras

    elif opcao == 4:
        print("Encerrando")
        break

    else:
        print("Opção inválida!")
