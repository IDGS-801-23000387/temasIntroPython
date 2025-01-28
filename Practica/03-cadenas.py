# Precio de cada boleto
precio_boleto = 12000

# Solicitar datos al usuario
nombre = input("Ingrese su nombre: ")
cantidad_boletos = int(input("¿Cuántos boletos desea comprar? (máximo 7): "))
tiene_tarjeta = input("¿Tiene tarjeta CINECO? (sí/no): ").strip().lower()

# Verificar que no se supere el máximo de boletos
if cantidad_boletos > 7:
    print("No puedes comprar más de 7 boletos.")
else:
    # Calcular el precio total sin descuentos
    total = cantidad_boletos * precio_boleto

    # Aplicar descuentos según la cantidad de boletos
    if cantidad_boletos > 5:
        descuento = total * 0.15
    elif 3 <= cantidad_boletos <= 5:
        descuento = total * 0.10
    else:
        descuento = 0

    # Restar el descuento inicial
    total -= descuento

    # Aplicar descuento adicional si tiene tarjeta CINECO
    if tiene_tarjeta == "sí":
        descuento_tarjeta = total * 0.10
        total -= descuento_tarjeta
    else:
        descuento_tarjeta = 0

    # Mostrar el total a pagar
    print("\nResumen de compra:")
    print(f"Nombre: {nombre}")
    print(f"Cantidad de boletos: {cantidad_boletos}")
    print(f"Descuento por cantidad de boletos: ${descuento:.2f}")
    print(f"Descuento por tarjeta CINECO: ${descuento_tarjeta:.2f}")
    print(f"Total a pagar: ${total:.2f}")j