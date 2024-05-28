var_verdade = True
var_falso = False

if var_verdade == True :
    print ("var verdade é: ", var_verdade)
    print ("Aqui continua no bloco do if")

#Comparacoes: == != > < >= <=
#Operadores: usa and e or no lugar de & e ||

if 1 > 2 :
    print("Um é maior que 2 ")
else:
    print("Um nao é maior que dois")


print("\n Opcoes: \n 1 Escreve guilherme \n 2 Escreve joao \n 3 Escreve maria")

opcao = input("Escolha uma opcao: ")
# Verificar se a entrada é um número válido
if opcao in ['1', '2', '3']:
    if opcao == '1':
        print("Guilherme")
    elif opcao == '2':
        print("João")
    elif opcao == '3':
        print("Maria")
else:
    print("Opcao invalida")

idade = 50
if idade == 50:
    print ("Voce tem 50 anos")
else:
    print ("Voce nao tem 50 anos")

if not idade == 50:
    print ("Voce nao tem 50 anos")
else: 
    print ("Voce tem 50 anos")

'''Faca um programa que pergunte a idade, peso e altura de 
uma pessoa e decide se ela esta apta a ser do exercito
Para entrar no exercicito tem q ter mais de 18, pesar > =60
e medir > =1,70
'''
print("***Exercicio da aula 3***\n")
#tem que converter os inputs para float ou int pq se nao é uma String
idade = int(input("Informe sua idade : "))
peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

if (idade >= 18 and peso >= 60 and altura >= 1.70):
    estarApto = True
    print("Voce esta apto a entrar no exercito")
else: 
    estarApto = False
    print("Voce nao esta apto a entrar no exercito")