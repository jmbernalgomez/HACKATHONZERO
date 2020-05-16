edad_usuario = input("Díganos su edad: ")
edad_usuario = int(edad_usuario)

if edad_usuario < 4:
    print("El precio de su entrada es gratis")
elif edad_usuario >= 4 and edad_usuario <=18:
    print("El precio de su entrada es 5€")
else:
    print("El precio de su entrada es 10€")