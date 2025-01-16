import os

def funcion1():
    os.system("cls")
    num1=int (input("Ingresa el primer número: "))
    num2=int (input("Ingresa el primer número: "))
    res=num1+num2
    print(f"Resultado:{res}")
    
    
def funcion2():
    num1=int (input("Ingresa el primer número: "))
    num2=int (input("Ingresa el primer número: "))
    res=num1-num2
    print(f"Resultado:{res}")

def funcion3():
    num1=int (input("Ingresa el primer número: "))
    num2=int (input("Ingresa el primer número: "))
    res=num1/num2
    print(f"Resultado:{res}")
    
def funcion4():
    num1=int (input("Ingresa el primer número: "))
    num2=int (input("Ingresa el primer número: "))
    res=num1*num2
    print(f"Resultado:{res}")
    
def run():
    while True:
        os.system("cls")
        print("1.Suma")
        print("2.Restar")
        print("3.Division") 
        print("4.Multiplicacion")  
        print("4.Salir")                
        op=int(input("Selecciona una opción: "))
        if op==1:
            funcion1()
        elif op==2:
            funcion2()
        elif op==3:
            funcion3()
        elif op==4:
            funcion4()
        else:
            exit()                


if __name__ == "__main__":
    run()