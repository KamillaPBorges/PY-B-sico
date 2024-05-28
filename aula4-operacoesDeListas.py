frase = 'Oi, tudo bem?'
lista_nomes = ["Joao", "Maria", "Guilherme", "Diego"]
lista_nomes.append("Geralda")
#o append add no ultimo lugar da lista
print(lista_nomes)
lista_nomes.remove("Joao")
print(lista_nomes)

lista_nomes.insert(1, "cleusa") #cleusa vira o segundo nome da lista
print(lista_nomes)
lista_nomes[0] = "Roberto"
print(lista_nomes)
contador_diego = lista_nomes.count("Diego")
print(contador_diego)

print(lista_nomes.pop())  #ultimo da lista e tira da lista
print(lista_nomes)

#Para string:
print(frase.lower())

#separa onde tiver a virgula
fraseSeparada =frase.split(',')   #transforma a string (frase) numa lista
print(fraseSeparada) #transformou a a frase numa lista com 2 
#componentes: oi e tudo bem, pq foi separado onde tinha a ','
print(fraseSeparada[0])

#o + concatena
frase_nova = frase + " como vai voce?"
print(frase_nova)