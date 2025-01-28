class OperasBas:
    # Declaramos el constructor this es el equivalente a self en python
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.res = 0
        
    # Declaracion de metodos de la clase
    def suma(self):
        self.res = self.num1 + self.num2
        print("la suma es: {}".format(self.res))
        
    def resta(self):
        self.res = self.num1 - self.num2
        print("la resta es: {}".format(self.res))

def main():
    obj = OperasBas(3, 4)
    obj.suma()
    obj.resta()
       
if __name__ == "__main__":
    main()
    
    """Resuleve un programa para la distancia de dos puntos en el plano cartesiano orientado a objetos 
    """
    