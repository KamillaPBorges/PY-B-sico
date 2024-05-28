print("Ola mundo")
print(len("ola mundo"))  # 9 caracteres

def funcao_soma(numero1, numero2):
    resp = numero1 + numero2
    return resp


variavel = funcao_soma(75, 29)
print(variavel)

def imprime_oi():
    print("Oi")

def tem_sete_letras(palavra):
    if len(palavra) == 7:
        return True
    else:
        return False
    
print(tem_sete_letras("oi pessoal"))
'''Escreva uma funcao que recebe um objeto
de colecao e retorna o maior numero dentra 
dessa colecao
faca outra funcao que retorna o menor
'''
def maior_numero (colecao):
    maior= colecao[0]
    for i in colecao:
        if i > maior:
            maior=i
    
    return maior
def menor_numero(colecao):
    menor = colecao[0]
    for i in colecao:
        if i < menor:
            menor = i
    return menor      


            
minha_tupla = ("3", "8")

maiorValor = maior_numero(minha_tupla)
print(maiorValor)
menorValor = menor_numero(minha_tupla)
print(menorValor)