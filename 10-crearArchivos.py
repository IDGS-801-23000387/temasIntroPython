from io import open 
import math 

lectura=""
texto=open("archivo.txt","r")
lectura=texto.readlines()
print(type(lectura))
print(lectura)
for linea in lectura:
    print(linea)
texto.close()