texto1="Hola"
texto2="Mundo"

textoFinal=texto1+texto2
print(textoFinal)
print("el saludo es: %s %s " %(texto1,texto2))

saludoFinal2="Saludo: {x} {y}".format(x=texto1, y=texto2)
print(saludoFinal2)

texto="Desarrollo Web Profesional Utl"
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title())
print(texto.find("eb"))
print(texto.count("U"))

print (texto.replace("e","a"))
cadenaSeparada=texto.split(" ")
print(cadenaSeparada)