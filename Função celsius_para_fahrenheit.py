def converter_temperatura(C):
    F = (C * 1.8) + 32
    return F
print("Vamos converter Celsius para Fahrenheit!")
C = float(input("Digite a temperatura em Celsius: "))
F = converter_temperatura(C)
print(f"A temperatura em Fahrenheit é: {F:.2f}°F")