from cliente import Cliente

class Conta:
    def __init__(self, Cliente, limite, saldo) :
        self.Cliente = Cliente
        self.limite = limite
        self.saldo = saldo

    def sacar(self, valor):
        if self.saldo < valor and valor > self.limite:
            print("Saldo ou limite insuficiente para o saque")
        else:
            self.saldo -= valor
    def depositar(self, valor)       :
        self.saldo += valor 