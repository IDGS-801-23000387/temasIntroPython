x=0
temp=""
while x<10:
    
    print(x)
    temp+=str(x)+"+"
    x+=1

""" Operaciom de Multiplicacion de a x b utilizansdo sumas  sumas
a=3
b=4
salida:3+3+3+3=12

"""


a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
resultado = 0
c=0
resFinal ="El Resultadio es:"
while c<b:
    
    resultado =resultado + a
    c= c+1
    resFinal+=str(a)+"+"    
resFinal+="="+str(resultado)
print(resFinal)
   
     