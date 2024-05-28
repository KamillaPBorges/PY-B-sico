class Veiculo:


    def __init__(self, cor, rodas, marca, tanque) :
        self.cor = cor  #quando iniciar a cor nos () joga sentro do self.cor
        self.rodas = rodas
        self.marca = marca
        self.tanque = tanque
    def abastecer(self, litros):
        self.tanque += litros    

    
   
#caracteristicas do veiculo
#self eh como se fosse o this
#self eh como se forr um parametros
#init é o costrutor

