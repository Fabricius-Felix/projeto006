import Veiculo

class Carro(Veiculo.Veiculo):
    def __init__(self, chassi, marca, modelo, ano, potencia, tipoCarro):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Carro")
        self.potencia = potencia
        self.tipoCarro = tipoCarro
        self.marcha = 0

    def ligar(self):
        return self.marcha

    def desligar(self):
        self.marcha = 0

    def trocar_marcha(self, nova_marcha):
        if nova_marcha >= 0 and nova_marcha <= 6:
            self.marcha = nova_marcha
            print(f"Marcha alterada para {nova_marcha}")
        else:
            print("Marcha inválida")

""" Aqui comeca o teste """
CarroNovo = Carro('8885AZKG01Z12A33921312', 'JAC', 'J3', '2022', 2.0, 'HATCH')
print(CarroNovo.get_tipo())
print(CarroNovo.potencia)
print(CarroNovo.tipoCarro)
print(CarroNovo.ligar())

""" Teste trocando a Marcha de carro """
CarroNovo.trocar_marcha(3) 
print("Nova marcha:", CarroNovo.ligar())
