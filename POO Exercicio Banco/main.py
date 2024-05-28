'''Crie um software de gerenciamento bancario
tera que criar clientes e contas
cada cliente tem nome, cpf e idade
cada conta possui um cliente e um saldo, limite
metodos sacar e dpositar
'''
from cliente import Cliente
from conta import Conta

kamilla = Cliente("Kamilla", "02375703006", 25 )
conta1 = Conta("kamilla", 50000, 2)

print("cliente: ", conta1.Cliente, " de limite: ", conta1.limite, " possui saldo: ", conta1.saldo)

conta1.depositar(500)
print("cliente: ", conta1.Cliente, " de limite: ", conta1.limite, " possui saldo: ", conta1.saldo)