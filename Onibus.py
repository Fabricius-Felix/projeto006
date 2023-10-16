import Veiculo
class Onibus( Veiculo.Veiculo ):
    def __init__(self, chassi, marca, modelo, ano, cilindrada, numero_rodas,qtd_portas ):
        super().__init__(chassi, marca, modelo, ano)
        super().set_tipo("Onibus")
        self.cilindrada = cilindrada
        self.numero_rodas = numero_rodas
        self.marcha = 1
        self.farol = 0  
        self.qtd_portas = qtd_portas
    def ligar( self ):
        return self.marcha
    def desligar( self ):
        self.marcha = 1
    
    def controlar_farol(self, estado):
        if estado == 0:
            self.farol = 0   
            print ("Farol Desligado")
        elif estado == 1:
            self.farol = 1   
            print ("Farol Baixo Ligado")
        elif estado == 2:
            self.farol = 2  
            print ("Farol Farol Alto Ligado")
        else:
            print("Estado inválido do farol")
""" Aqui comeca o teste """
OnibusNovo = Onibus('5AZKG01Z12A339037', 'Honda', 'CG', '2015', 1200, 6 , 3)
print(OnibusNovo.get_tipo())  
print(OnibusNovo.numero_rodas)
print(OnibusNovo.marca)
print(OnibusNovo.ligar())

OnibusNovo.controlar_farol(1)
print("Estado do farol:", OnibusNovo.controlar_farol)


