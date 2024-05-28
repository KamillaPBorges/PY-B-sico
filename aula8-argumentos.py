import sys #biblioteca



def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

argumentos = sys.argv 
#arg 1 metodo 
#arg 2 n1
#arg 3 n2
print(argumentos)
if argumentos[1] == "soma":
    resp= soma(float(argumentos[2]), float(argumentos[3]))
elif argumentos[1] == "sub":
    resp = sub (argumentos[2], argumentos[3])
print (resp)