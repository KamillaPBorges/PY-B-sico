import time
try:
    a = 1200 / 0  #tenta
except ZeroDivisionError:
    print("Divisao por zero, nao da pra fazer")


try:
    asfiosj()
except Exception as err: #Pode ser qualquer exceçao
    print("aconteceu alguma coisa errada", err)
#Para dizer qual erro coloca as alguma coisa e printa
#para saber o que é


def abre_arquivo():
    try:
        arquivo = open("arquivo.txt")
        return True
    except Exception as erro:
        print("Aconteceu algum erro", erro)
        return False #se n conseguir abrir retorna false
while not abre_arquivo():
    print("tentando abrir o arquivo")
    time.sleep(5) #tenta abri o arquivo a cada 5 segundos
print("Conseguiu abri arquivo")
     