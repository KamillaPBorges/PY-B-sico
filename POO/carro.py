from veiculo import Veiculo
class Carro(Veiculo):
    def __init__(self, cor, rodas, marca, tanque) :

        Veiculo.__init__(self, cor, 4, marca, tanque)
    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print("Erro no abastecimento")
        else:
            self.tanque += litros

'''Crie um software de gerenciamento bancario
tera que criar clientes e contas
cada cliente tem nome, cpf e idade
cada conta possui um cliente e um saldo, limite
metodos sacar e dpositar
'''