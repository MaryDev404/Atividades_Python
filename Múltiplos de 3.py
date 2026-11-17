for i in range(1,51):
    if i % 3 == 0:
        print("O número", i, "é múltiplo de 3")
print("Agora é sua vez! Escolha um número inteiro e descubra se ele é múltiplo de 3.")
numero = int(input("Digite um número inteiro: "))
if numero % 3 == 0:
    print(f"O número {numero} é múltiplo de 3.")
else:
    print(f"O número {numero} não é múltiplo de 3.")