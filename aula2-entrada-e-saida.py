print()  #sempre imprime uma String o print
print('hello world - pode ser com aspas simples')
print("hello world - pode ser com aspas duplas")
nome = 'Kamilla' 
print(nome)
tipo = type (nome)
print(tipo)   #objeto do tipo String

idade = 25
tipo_idade = type(idade)
print (tipo_idade)  #objeto do tipo int 

altura = 1.60
tipo_altura = type(altura)
print(tipo_altura)

# pode concatenar usando virgula ou +, mas no python eh 
#melhor usar , para que ja converta para string pro print
print(nome, "tem", idade, "anos")  #kamilla tem 25 anos
print("Para converter um tipo para String: str(..)")
str(idade)
print(idade) 

nome = input("Escreva seu nome: ")
#o que ta dentro dos parenteses eh o argumento
#nao precisa necessariamente de argumento
altura = input("Escreva sua altura: ")
print(nome, "tem", altura, "de altura")
#input sempre retorna um objeto tipo String

print (type(altura))