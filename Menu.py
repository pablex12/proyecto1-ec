import pywhatkit

usuarios = []

#########################################################################


def opcion_1():
    while True:
        nombre = input("Ingrese su nombre:\n")
        if nombre.isalpha() != True:
            print("¡La entrada no es valida. Ingrese su nombre nuevamente!")
        else:
            break

    while True:
        apellido = input("Ingrese su apellido:\n")
        if apellido.isalpha() != True:
            print("¡La entrada no es valida. Ingrese su apellido nuevamente!")
        else:
            break

    while True:
        genero = input(
            "Inserte M para masculino, F para femenino y N si no desea indicarlo:\n")
        if genero.lower() in ["m", "f", "n"]:
            break
        else:
            print("¡La entrada no es valida. Ingrese su genero nuevamente!")

    while True:
        numero_tel = input("Ingrese su numero de telefono (+506):\n")
        if numero_tel.isalpha() == True:
            print("¡La entrada no es valida. Ingrese su numero nuevamente!")
        elif numero_tel.startswith("+506") == False:
            print(
                "Recuerde acompañar el numero con (+506). Ingrese su numero nuevamente.")
        else:
            break

    while True:
        try:
            monto_in = input("Ingrese su monto inicial: \n")
            if monto_in.isalpha() == True:
                print("¡La entrada no es valida. Ingrese el monto nuevamente!")
            else:
                monto_in_int = float(monto_in)
                monto_in_int = int(monto_in_int)
                break
        except:
            print("¡La entrada no es valida. Ingrese el monto nuevamente!")

    return {
        "id": len(usuarios),
        "nombre": nombre,
        "apellido": apellido,
        "genero": genero,
        "telefono": numero_tel,
        "monto": monto_in_int
    }


def opcion_2():
    while True:
        usuario1, usuario2 = None, None

        if len(usuarios) <= 1:
            print("¡No hay suficientes usuarios registrados!")
            break

        id_usuario1 = int(
            input("Ingrese su ID o número de cuenta de la que va a retirar el dinero:\n"))

        while True:

            for usuario in usuarios:
                # print(usuario)
                if id_usuario1 in usuario.values():
                    print("Usuario seleccionado es:\n")
                    usuario1 = usuario
                    print(usuario["nombre"])

                    break

            if usuario1:
                break
            else:
                print("¡El usuario no existe!")
                break

        # print(usuario1)

        if usuario1:
            id_usuario2 = int(
                input("Ingrese el ID o número de cuenta destino:\n"))

            if id_usuario1 == id_usuario2:
                print("No puede ser el mismo usuario")
                break

            while True:

                for usuario in usuarios:
                    # print(usuario)
                    if id_usuario2 in usuario.values():
                        print("Usuario seleccionado es:\n")
                        usuario2 = usuario
                        print(usuario["nombre"])
                        break

                if usuario2:
                    break
                else:
                    print
                    ("¡El usuario no existe!")
                    break

        if usuario1 and usuario2:
            # print(usuario1, usuario2)
            dinero_depositar = int(input("Cantidad de dinero a depositar: "))
            if usuario1["monto"] - dinero_depositar < 0:
                print("¡Fondos insuficientes!")
            else:
                usuario1["monto"] = usuario1["monto"] - dinero_depositar
                usuario2["monto"] = usuario2["monto"] + dinero_depositar
                usuarios[id_usuario1] = usuario1
                usuarios[id_usuario2] = usuario2
                print("El monto", dinero_depositar,
                      "fue depositado en la cuenta de", usuario2["nombre"])
                break


def opcion_3():
    if len(usuarios) == 0:
        print("¡No hay usuarios registrados!")
    else:
        msj = ""
        for usuario in usuarios:
            msj += "La cuenta de " + \
                usuario["nombre"]+" "+usuario["apellido"]+"\n"
            msj += "Tiene el id: "+str(usuario["id"]) + "\n"
            msj += "Monto de la cuenta: "+str(usuario["monto"])+"\n\n"

        desis = input("¿Quiere enviar el mensaje por Whatsapp? (si o no)\n")
        if desis.lower() == "no":
            print(msj)
        elif desis.lower() == "si":
            while True:
                telef = input(
                    "Ingrese el numero al que desea enviar el mensaje (+506):\n")
                if (telef.startswith("+506") != False):
                    pywhatkit.sendwhatmsg_instantly(telef, msj)
                    print("Mensaje enviado con exito!")
                    break
                else:
                    print(
                        "¡Recuerde acompañar el numero con (+506) o la entrada es inválida. Ingrese su numero nuevamente!")

        else:
            print("¡Entrada invalida, ingrese su respuesta nuevamente!")
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
    while True:
        try:
            opcion_user = int(
                input("Bienvenido, cuál opción del 1 al 5 desea realizar?\n"))
            break
        except:
            print(
                "¡El valor ingresado no corresponde a una opción del menú. Vuélvalo a intentar!")

    # Opciones del menú
    if opcion_user == 1:
        usuario = opcion_1()
        incluir_usuario(usuario)


########################################################################

    if opcion_user == 2:
        opcion_2()

########################################################################

    if opcion_user == 3:
        opcion_3()

########################################################################

    if opcion_user == 4:
        pass

    if opcion_user == 5:
        print("Saliendo del programa...")
        break

    elif opcion_user > 5:
        print(
            "¡El valor ingresado no corresponde a una opción del menú. Vuélvalo a intentar!")

########################################################################
