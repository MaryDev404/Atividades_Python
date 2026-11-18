while True:
    print("\n--- MENU DE OPÇÕES ---")
    print("1. Converter Celsius para Fahrenheit")
    print("2. Converter km para milhas")
    print("3. Converter kg para libras")
    print("4. Sair")
    
    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
         def converter_temperatura(C):
            F = (C * 1.8) + 32
            return F
         print("")
         print("Vamos converter Celsius para Fahrenheit!")
         C = float(input("Digite a temperatura em Celsius: "))
         F = converter_temperatura(C)
         print(f"A temperatura em Fahrenheit é: {F:.2f}°F")

    elif opcao == "2":
       def converter_km_para_milhas(km):
        conversao = 0.621371
        return km * conversao
       print("")
       distancia_km = float(input("Digite a distância em quilômetros (km): "))
       resultado_milhas = converter_km_para_milhas(distancia_km)
       print(f"{distancia_km} km equivalem a {resultado_milhas:.2f} milhas.")

    elif opcao == "3":
       def converter_kg_para_libras(kg):
        conversao = 2.20462
        return kg * conversao
       print("")
       peso_kg = float(input("Digite o peso em quilogramas (kg): "))
       resultado_libras = converter_kg_para_libras(peso_kg)
       print(f"{peso_kg} kg equivalem a {resultado_libras:.2f} libras.")


    elif opcao == "4":
        print("\nSaindo do programa... Até logo!")
        break
    else:
        print("\nOpção inválida! Por favor, escolha 1, 2, 3 ou 4.")