import Veiculo

class Caminhao(Veiculo.Veiculo):
    def __init__(self, chassi, marca, modelo, ano, potencia, tipoCaminhao, altura, eixos, quilometragem):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Caminhao")
        self.potencia = potencia
        self.tipoCaminhao = tipoCaminhao
        self.marcha = 1
        self.altura = altura
        self.eixos = eixos
        self.quilometragem = quilometragem

    def ligar(self):
        return self.marcha

    def desligar(self):
        self.marcha = 0

    def trocar_marcha(self, nova_marcha):
        if self.tipoCaminhao == "Bitrem":
            if nova_marcha >= 1 and nova_marcha <= 12:
                self.marcha = nova_marcha
                print(f"Marcha alterada para {nova_marcha}")
            else:
                print("Marcha inválida para um caminhão Bitrem")
        else:
            if nova_marcha >= 1 and nova_marcha <= 6:
                self.marcha = nova_marcha
                print(f"Marcha alterada para {nova_marcha}")
            else:
                print("Marcha inválida para um caminhão comum")

""" Aqui comeca o teste """
CaminhaoNovo = Caminhao('PM2B200S003402403', 'Mercedes-Benz', 'Atego 2430', '2018', 7.2, 'Bitrem', 1.80, 7, 757930)
print(CaminhaoNovo.get_tipo())
print(CaminhaoNovo.potencia)
print(CaminhaoNovo.tipoCaminhao)
print(CaminhaoNovo.ligar())

# Executando o método trocar_marcha
CaminhaoNovo.trocar_marcha(6)  # Trocar para a sexta marcha
print("Nova marcha:", CaminhaoNovo.ligar())
