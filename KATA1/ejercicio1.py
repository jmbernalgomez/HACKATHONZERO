# Ejercicio 1

precio = 3.49
descuento = 1 - 0.60
precio_con_descuento = precio * descuento
 
numero_de_barras = input("Introduce el número de barras vendidas: ")
numero_de_barras = int(numero_de_barras)

# print("Precio habitual: " + str(precio))
# print("Descuento: " + str(precio_con_descuento))
# print("Coste final: " + str(numero_de_barras * precio_con_descuento))

print(f"Precio habitual: {precio}")
print(f"\nDescuento: {precio_con_descuento}")
print(f"\nCoste final: {numero_de_barras * precio_con_descuento}")

# Ejercicio 2

password = "contraseña"

password_usuario = input("Introduzca la contraseña: ")

if password == password_usuario:
    print(f"SON IGUALES")
else:
    print(f"NO SON IGUALES")
