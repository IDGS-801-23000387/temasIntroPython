""" 
Programa para distancia de de dos puntos en el plano cartesiano
"""
class OperasBas:
    res=0
   
    # Declaramos el constructor this es el equivalente a self en python
    def __init__(self, punt1=0, punt2=0, punto1=0, punto2=0):
        self.punt1 = punt1
        self.punt2 = punt2  
        self.punto1 = punto1    
        self.punto2 = punto2
        self.res = 0
        
    def pedirDatos(self):
        self.punt1 = int(input("Ingresa el primer punto : "))
        self.punt2 = int(input("Ingresa el segundo punto : "))
        self.punto1 = int(input("Ingresa el primer punto : "))
        self.punto2 = int(input("Ingresa el segundo punto : "))
        
    # Declaracion de metodos de la clase
    def operacion(self):
        self.res = ((self.punt1 - self.punto1)**2 + (self.punt2 - self.punto2)**2)**0.5
        print("la distancia es: {}".format(self.res))   
        
def main():
    obj = OperasBas()
    obj.pedirDatos()
    obj.operacion()
    
if __name__ == "__main__":
    main()