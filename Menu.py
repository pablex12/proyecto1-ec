import pywhatkit
from os import system
Jose Pablo Herrera Vargas
# 0143


Hola,
Santillana
. ¡Saluda!
— 15/03/2023 17: 52
KüroKatzê
está aquí.
— 16/03/2023 7: 55
Santillana — 18/03/2023 15: 05
https: // tipodecambio.paginasweb.cr/api
fg4VHDD40PxLM4aqcwEq5ArXlWOszva5
https: // api.apilayer.com/exchangerates_data/convert?to = CRC & from = EUR & amount = 1
KüroKatzê — 18/03/2023 19: 45

#########################################################################


def opcion_1():
    while True:
        nombre = input("Ingrese su nombre:\n")


Expandir
proyecto_1.py
4 KB
Jose Pablo Herrera Vargas — ayer a las 12: 42

usuarios = []

#########################################################################
Expandir
Menu.py
4 KB
Santillana — ayer a las 15: 14

usuarios = []

#########################################################################
Expandir
Lab.1.2.py
5 KB
KüroKatzê — hoy a las 14: 15

usuarios = []

#########################################################################


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
            print("La entrada no es valida. Ingrese su numero nuevamente.")
        elif numero_tel.startswith("+506") == False:
            print("Recurde acompañar el numero con (+506). Ingrese su numero nuevamente.")
        else:
            break

    while True:
        monto_in = input("Ingrese su monto inicial: \n")
        if monto_in.isalpha() == True:
            print("La entrada no es valida. Ingrese el monto nuevamente.")
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

########################################################################

    if opcion_user == 2:
        pass

########################################################################
... (43 líneas restantes)
Contraer
Lab.1.2.py
5 KB
﻿

usuarios = []

#########################################################################


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
            print("La entrada no es valida. Ingrese su numero nuevamente.")
        elif numero_tel.startswith("+506") == False:
            print("Recurde acompañar el numero con (+506). Ingrese su numero nuevamente.")
        else:
            break

    while True:
        monto_in = input("Ingrese su monto inicial: \n")
        if monto_in.isalpha() == True:
            print("La entrada no es valida. Ingrese el monto nuevamente.")
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

########################################################################

    if opcion_user == 2:
        pass

########################################################################

    if opcion_user == 3:
        if len(usuarios) == 0:
            print("No hay usuarios registrados")
        else:
            msj = ""
            for usuario in usuarios:
                msj += "La cuenta de " + usuario["nombre"] + "\n"
                msj += "Tiene el id:"+str(usuario["id"]) + "\n"
                msj += "Monto de la cuenta:"+str(usuario["monto"])+"\n"

            desis = input(
                "¿Quiere enviar el mensaje por Whatsapp? (si o no)\n")

            if desis.lower() == "no":
                print(msj)

            elif desis.lower() == "si":
                telef = input(
                    "Ingrese el numero al que desea enviar el mensaje (+506):\n")

                if telef.startswith("+506") != False:
                    pywhatkit.sendwhatmsg_instantly(telef, msj)
                    print("Mensaje enviado con exito!")

                else:
                    print(
                        "Recurde acompañar el numero con (+506). Ingrese su numero nuevamente.")

            else:
                print("Entrada invalida, ingrese su respuesta nuevamente")
            break

########################################################################

    if opcion_user == 4:
        pass

    if opcion_user == 5:
        print("Saliendo del programa...")
        break

    elif opcion_user > 5:
        print("El valor ingresado no corresponde a una opción del menú")

########################################################################
