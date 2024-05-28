
#Coleções -> Estruturas de Dados
minha_lista = ["Gui", "Joao"] #lista[]
#lista eh ordenada, cada objeto ocupa uma posicao

minha_tupla = ("Gui", "Joao")  #tupla()
#tupla nao pode adicionar e remover objetos
#tupla nao pode mudar o tamanho, tem indices

meu_dicionario = {"Nome": "Guilherme", "idade": 25} #dicionario{}
#chave e valor
#chave palavra e valor o significado
print(meu_dicionario)

meu_conjunto = {"Gui", "Joao"} 
#conjunto eh uma lista sem itens repetidos
#conjunto nao eh ordenado, nao tem indice
#conjunto -> set


print(type(minha_tupla))
print(minha_tupla[1])
for i in minha_tupla:
    print(i)

minha_tupla = {"Joao", "Fabricio"} #substitui toda a dupla

if "Fabricio" in minha_tupla:
    print("Fabricio esta na colecao")



print(meu_dicionario["Nome"]) #imprime guilherme
print(len(meu_dicionario)) # tem duas coisas nome e guilherme

if "Guilherme" in meu_dicionario.values():
    print("Guilherme esta no dicionario")

for i in meu_dicionario.values():
    print(i)
for i in meu_dicionario.keys():
    print(i)

#Para adicionar no dicionario
meu_dicionario["Endereço" ] = "Silveira Martins"
print(meu_dicionario)
meu_dicionario["Telefone: "] = "32311861"

#Conjuntos
#Conjunto eh melhor de pesquisar que lista
meu_conjunto.add("Maria")
print(meu_conjunto)
if "Gui" in meu_conjunto:
    print("Gui foi encontrado na lista")
meu_conjunto.remove("Gui")

loucura = [(1,2), (3,4), (5,6)]
print(loucura) #eh umaq lista
