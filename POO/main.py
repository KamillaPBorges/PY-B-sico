from veiculo import Veiculo
#dentro da arquivo veiculo importa a classe Veiculo
from carro import Carro

caminhao_rosa = Veiculo ("rosa", 6, "ford", 10)
print(caminhao_rosa.cor)
print(type(caminhao_rosa))
carro_azul = Carro("azul", 56, "ford", 18)

print( " cor: ", caminhao_rosa.cor, " marca: ", caminhao_rosa.marca, " quantidade do tanque: ", caminhao_rosa.tanque)

caminhao_rosa.abastecer(34)
print("Tanque apos abastecimento: ", caminhao_rosa.tanque)
