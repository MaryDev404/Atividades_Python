numero = int(input("Digite um número inteiro: "))

while True:
    if numero % 2 == 0:
        print(f"O número {numero} é PAR.")
    else:
        print(f"O número {numero} é ÍMPAR.")
    continuar = input("Deseja verificar outro número? (s/n): ")
    if continuar.lower() != "s":
        break
    numero = int(input("Digite um número inteiro: "))
    continue