import os
from person import Persona

salir = 1
accionesPermitidas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listaPersonas = []


def mostrarMenu():
    print("1. Ingresar persona.")
    print("2. Mostrar personas")
    print("3. Eliminar persona.")
    print("4. Modificar apellido.")
    print("5. Modificar direccion.")
    print("6. Agregar vacunas.")
    print("7. Modificar vanuca.")
    print("8. Eliminar vacuna.")
    print("9. Salir.\n")


def limpiarTerminal():
    if os.name == 'nt':
        os.system('cls')  # for windows
    else:
        os.system('clear')  # for linux or mac


def continuar():
    respuesta = int(input("Desea realizar otra accion? [ingrese 0 para si]: "))
    if respuesta == 0:
        limpiarTerminal()
    else:
        global salir
        salir = 0


def ejecutarAccion(accion):
    match accion:

        case 1:
            dni = int(input("DNI: "))
            nombre1 = input("PRIMER NOMBRE: ")
            nombre2 = input("SEGUNDO NOMBRE [DEJAR EN BLANCO SI NO TIENE]: ")
            if nombre2 != "":
                nombre3 = input(
                    "TERCER NOMBRE [DEJAR EN BLANCO SI NO TIENE]: ")
            else:
                nombre3 = ""
            if nombre2 and nombre3 != "":
                nombre4 = input(
                    "CUARTO NOMBRE [DEJAR EN BLANCO SI NO TIENE]: ")
            else:
                nombre4 = ""
            apellido1 = input("APELLIDO: ")
            apellido2 = input(
                "SEGUNDO APELLIDO [DEJAR EN BLANCO SI NO TIENE]: ")
            if apellido2 != "":
                apellido3 = input(
                    "TERCER APELLIDO [DEJAR EN BLANCO SI NO TIENE]: ")
            else:
                apellido3 = ""
            direccion = input("DIRECCION: ")
            telefono = input("TELEFONO: ")
            persona = Persona(dni, nombre1, nombre2, nombre3, nombre4,
                              apellido1, apellido2, apellido3, direccion, telefono)
            listaPersonas.append(persona)
            continuar()

        case 2:
            print("##### LISTA DE PERSONAS #####")
            for i in range(len(listaPersonas)):
                print(f"Persona {i}. {listaPersonas[i]}")
            continuar()

        case 3:
            print("##### LISTA DE PERSONAS #####")
            for i in range(len(listaPersonas)):
                print(f"Persona {i}. {listaPersonas[i]}")
            nroPersona = int(
                input("Ingrese el numero de la persona a eliminar: "))
            while nroPersona > len(listaPersonas) or nroPersona < 0:
                print("ERROR: El valor ingresado no es valido")
                nroPersona = int(input("Intente nuevamente: "))
            print(f"\nUsted selecciona la persona: {
                  nroPersona}. {listaPersonas[nroPersona]}")
            del listaPersonas[nroPersona]
            continuar()

        case 4:
            print("##### LISTA DE PERSONAS #####")
            for i in range(len(listaPersonas)):
                print(f"Persona {i}. {listaPersonas[i]}")
            nroPersona = int(
                input("Ingrese el numero de la persona a modificar: "))
            while nroPersona > len(listaPersonas) or nroPersona < 0:
                print("ERROR: El valor ingresado no es valido")
                nroPersona = int(input("Intente nuevamente: "))
            listaPersonas[nroPersona].modificarApellidos()
            continuar()

        case 5:
            dni = int(input("Ingrese el DNI de la persona: "))
            for i in range(len(listaPersonas)):
                if listaPersonas[i].dni == dni:
                    listaPersonas[i].modificarDireccion()
                else:
                    print("No se encontro el DNI ingresado.")

            continuar()

        case 6:
            print("eligio la opcion 6")
            continuar()

        case 7:
            print("eligio la opcion 7")
            continuar()

        case 8:
            print("eligio la opcion 8")
            continuar()

        case 9:
            global salir
            salir = 0


if __name__ == "__main__":

    while salir:
        mostrarMenu()
        accion = int(input("Ingrese el numero de accion que desea realizar: "))

        while accion not in accionesPermitidas:
            print("Error: no ingreso una accion valida.")
            accion = int(input("Intente nuevamente: "))
        ejecutarAccion(accion)
