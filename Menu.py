from os import system

usuarios = []

################################################################


def opcion_1():
    while True:
        nombre = input("Ingrese su nombre:\n")
        if nombre.isalpha() != True:
            print("La entrada no es valida. Ingrese su nombre nuevamente.")
        else:
            break
    while True:
        apellido = input("Ingrese su apellido:\n")
        if apellido.isalpha() != True:
            print("La entrada no es valida. Ingrese su apellido nuevamente.")
        else:
            break
    while True:
        genero = input(
            "Inserte M para masculino, F para femenino y N si no desea indicarlo:\n")
        if genero.lower() in ["m", "f", "n"]:
            break
        else:
            print("La entrada no es valida. Ingrese su genero nuevamente.")

    while True:
        numero_tel = input("Ingrese su numero de telefono (+506):\n")
        if numero_tel.isalpha() == True:
            print("La entrada no es valida. Ingrese su genero nuevamente.")
        elif numero_tel.startswith("+506") == False:
            print("Recurde acompañar el numero con (+506). Ingrese su genero nuevamente.")
        else:
            break

    while True:
        monto_in = input("Ingrese su monto inicial: \n")
        if monto_in.isalpha() == True:
            print("La entrada no es valida. Ingrese su genero nuevamente.")
        else:
            monto_in_int = float(monto_in)
            monto_in_int = int(monto_in_int)
            break

    return {
        "id": len(usuarios),
        "nombre": nombre,
        "appelido": apellido,
        "genero": genero,
        "telefono": numero_tel,
        "monto": monto_in_int
    }
########################################################################

########################################################################


def incluir_usuario(usuario):
    usuarios.append(usuario)
########################################################################


########################################################################
while True:
    # Opciones a elegir por el usuario
    print("_"*100)
    print("Seleccione una opción: ")
    print("1. Crear Usuario.")
    print("2. Realizar transacción de una cuenta a otra.")
    print("3. Reporte de información de clientes.")
    print("4. Tipo de cambio del día.")
    print("5. Salir del programa.")
    print("_"*100)
    print()

    # Si el usuario ingresa un valor string capture el error.
    try:
        opcion_user = int(
            input("Bienvenido, cuál opción del 1 al 5 desea realizar?\n"))
    except:
        print(
            "El valor ingresado no corresponde a una opción del menú",
        )
        continue

    # Opciones del menú
    if opcion_user == 1:
        usuario = opcion_1()
        incluir_usuario(usuario)
        print(usuarios)

    if opcion_user == 2:
        pass

    if opcion_user == 3:
        pass

    if opcion_user == 4:
        pass

    if opcion_user == 5:
        print("Saliendo del programa...")
        break

    elif opcion_user > 5:
        print("El valor ingresado no corresponde a una opción del menú")
