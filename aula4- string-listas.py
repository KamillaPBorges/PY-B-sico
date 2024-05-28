frase = 'Oi tudo bem?'
print (frase)
print("Se quisermos imprimir pedacos especificos da frase :")
print (frase[0], "é o primeiro caractere da frase")
print("Para imprimir de tal posicao ate tal posicao usa : ")
print(frase[0:5], "são os primeiros 6 caracteres da frase")

#para pular de 2 em 2 os caracteres -> step add :2 no fim
print(frase[0:8:2])  #comeca no 0, vai ate 8 e pula de 2 em 2
#para inverte pode o step ::-1
print(frase[::-1])
#lista eh uma colecao
lista_nomes = ["Joao", "Maria", "Guilherme", "Diego"]
tipoDaListaNomes = type(lista_nomes)
print(tipoDaListaNomes)   #tipo lista

print(lista_nomes[0], " eh primeiro indice da lista")
print(lista_nomes, "imprimiu a lista inteira se nao utilizar os colchetes")
print(lista_nomes[0:2]) #imprime o 0 e 1
#se quiser imprimir o ultimo valor usa o -1
print(lista_nomes[-1])   #imprime o diego pq eh o ultimo
print(lista_nomes[-1:-5:-1])  #inverte 