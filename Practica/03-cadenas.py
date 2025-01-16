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
def run():
    while True:
        print("Menú de opciones:")
        print("1. Suma")
        print("2. Resta")
        print("3. Division")
        print("4. Multiplicacion")
        print("5. Salir")
        
        op = int(input("Selecciona una opción: "))
        
        if op == 1:
            funcion1()
        elif op == 2:
            funcion2()
        elif op == 3:
            funcion3()
        elif op == 4:
            funcion4()
        elif op == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == "__main__":
    run()