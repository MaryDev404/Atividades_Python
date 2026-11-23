class Carros:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print("-" * 80)

car1 = Carros("Chevrolet", "Impala SS", 1967)
car2 = Carros("Ford", "Mustang Fastback", 1969)

car1.exibir()
car2.exibir()