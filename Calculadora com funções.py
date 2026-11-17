#Calculadora feita com funções

def somar(a,b): return a + b
def subtrair(a, b): return a - b
def multiplicacao(a, b): return a * b
def dividir(a, b):
    if b == 0: return "Erro!"
    return a / b

while True:
    op = input("Operação (+--*/0): ")
    if op == "0": break
    a = float(input("Num 1: "))
    b = float(input("Num 2: "))

    #chamar conforme 'op'