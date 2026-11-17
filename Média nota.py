while True:
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    nota4 = int(input("Digite a quarta nota:"))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 7:
        print("Aprovado!!:", media)
    else:
        print("Reprovado, não atingiu a média mínima:", media)
    continue_input = input("Deseja calcular a média de outro aluno? (s/n): ")
    if continue_input == "s":
        continue
    else:
        break