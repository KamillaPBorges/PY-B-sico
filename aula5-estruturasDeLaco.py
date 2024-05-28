nomes = ["Guilherme", "Marcelo", "Joao", "Julia"]
print(nomes)
print(nomes[0])
#Crie um programa que mostre os nomes um por um
for i in nomes:   #para cada i(nome) em nome
   print(i)

for nome in nomes:
   print(nome)

for i in range(4):
    print(nomes[i])
    

lista_de_numero = range(5) #cria uma lista com 5 numeros
for i in lista_de_numero:
    print(i)
lista_numeros = range(5, 10) #começa no 5 e termina no 10
for i in lista_numeros:
   print(i)         #vai do 5, 6, 7, 8 e 9
lista_numeros_step = range(0, 100, 2) #imprime de dois em doi ate 99
for i in lista_numeros_step:
   print(i)

palavra = "Guilherme Jungueira"   #String é uma coleção
for i in palavra:
   print(i)

i = 0
while i < 10:
    print('i ainda é menor que 10:', i)
    i += 1  # é o i++

print("Acabou o while, quando i for ", i)

lista_frutas= ["maca", "pera", "uva", "abacaxi"]
contador = 0
for fruta in lista_frutas:
   contador += 1
print(contador)
print(len(lista_frutas))  #tamanho da lista
print("Break para sair da estrutura de repeticao")

numero = 0
while True:
   print(numero)
   if numero == 20:
      break   #para com 20
   numero += 2
print("Saiu do while")
