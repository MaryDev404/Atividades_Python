while True:
    print("\n--- MENU DE OPÇÕES ---")
    print("1. Mostrar mensagem de boas-vindas")
    print("2. Fazer um cálculo")
    print("3. Sair")
    
    opcao = input("Escolha uma opção (1-3): ")


    if opcao == "1":
        print("\nOlá! Boas-vindas ao meu programa.")
    elif opcao == "2":
        print("")
        print("Vamos fazer um adição!")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        soma = num1 + num2
        resultado = soma
        print(f"\nO resultado de {num1} + {num2} = {resultado}")
    elif opcao == "3":
        print("\nSaindo do programa... Até logo!")
        break
    else:
        print("\nOpção inválida! Por favor, escolha 1, 2 ou 3.")