class Cinepolis:
    precioBoleto = 12

    def ejecutar(self):
        with open("ventas.txt", "w") as archivo:
            archivo.write("")   

        while True:
            print("\n--- Bienvenidos a Cinepolis ---")
            print("1. Comprar boletos")
            print("2. Terminar programa")
            opcion = int(input("Selecciona una opción: "))

            if opcion == 1:
                nombre = input("Ingresa tu nombre: ")

                while True:
                    numPersonas = int(input("¿Cuántas personas van contigo? "))
                    if numPersonas > 0:
                        break
                    print("Debe haber al menos una persona para comprar boletos.")

                while True:
                    maxBoletos = numPersonas * 7
                    numBoletos = int(input(f"¿Cuántos boletos quieres comprar?  : "))

                    if numBoletos < 1:
                        print("Debes comprar al menos 1 boleto.")
                    elif numBoletos > maxBoletos:
                        print(f"Solo puedes comprar hasta {maxBoletos} boletos.")
                        cambiar = input("¿Quieres cambiar el número de personas? (si/no): ").lower()
                        if cambiar == "si":
                            numPersonas = int(input("Ingresa el nuevo número de personas: "))
                        else:
                            print("Debes reducir la cantidad de boletos.")
                    else:
                        break 

                metodoPago = input("¿Vas a pagar con tarjeta CINECO o efectivo? (cineco/efectivo): ").lower()

                subtotal = numBoletos * self.precioBoleto
                descuento = 0.15 if numBoletos > 5 else (0.10 if numBoletos >= 3 else 0)
                if metodoPago == "cineco":
                    descuento += 0.10

                total = round(subtotal - (subtotal * descuento), 2)

                print("\n--- Resumen de la compra ---")
                print(f"Nombre: {nombre}")
                print(f"Boletos: {numBoletos}")
                print(f"Total a pagar: ${total:.2f}")
                print(f"Método de Pago: {metodoPago}")

                with open("ventas.txt", "a") as archivo:
                    archivo.write(f"{nombre},{numBoletos},{total:.2f},{metodoPago}\n")

            elif opcion == 2:
                self.mostrar_ventas()
                break
            else:
                print("Opción inválida. Intenta de nuevo.")

    def mostrar_ventas(self):
        total_ventas = 0   
        print("\n--- Historial de Ventas ---")

        with open("ventas.txt", "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(',')   
                nombre = datos[0]   
                total = float(datos[2])   

                total_ventas += total   
                print(f"Nombre: {nombre}, Total: ${total:.2f}")   

        print(f"\n--- Total de todas las ventas: ${total_ventas:.2f} ---")   


 
if __name__ == "__main__":
    Cinepolis().ejecutar()
