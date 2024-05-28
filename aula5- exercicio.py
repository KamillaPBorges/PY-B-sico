'''Facao um programa q leia a quantidade de pessoas que serao
convidadas para uma festa.
Apos isso ira perguntar de todas as pessoas e colocar numa lista de convidados
apos isso ira imprimir todos os nomes da lista
'''
qtde = 0
listaConvidados = []

while (qtde < 5):
    convidado = input("Informe o nome:")
    listaConvidados.append(convidado)
    qtde += 1
print(listaConvidados)


