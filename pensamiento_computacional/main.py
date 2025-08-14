import os
from person import Persona

testPerson = Persona(1,"a","b","","","c","d","","as 12",1123)

salir = 1
accionesPermitidas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listaPersonas = [testPerson]


def mostrarMenu():
    print("1. Ingresar persona.")
    print("2. Mostrar personas")
    print("3. Eliminar persona.")
    print("4. Modificar apellido.")
    print("5. Modificar direccion.")
    print("6. Agregar vacunas.")
    print("7. Modificar vancua.")
    print("8. Eliminar vacuna.")
    print("9. Salir.\n")


def limpiarTerminal():
    if os.name == 'nt':
        os.system('cls')  # for windows
    else:
        os.system('clear')  # for linux or mac


def continuar():
    respuesta = input("Desea realizar otra accion? [ingrese s para si]: ")
    if respuesta == "s" or respuesta == "S":
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
                nombre3 = input("TERCER NOMBRE [DEJAR EN BLANCO SI NO TIENE]: ")
            else:
                nombre3 = ""
            if nombre2 and nombre3 != "":
                nombre4 = input("CUARTO NOMBRE [DEJAR EN BLANCO SI NO TIENE]: ")
            else:
                nombre4 = ""
            apellido1 = input("APELLIDO: ")
            apellido2 = input("SEGUNDO APELLIDO [DEJAR EN BLANCO SI NO TIENE]: ")
            if apellido2 != "":
                apellido3 = input("TERCER APELLIDO [DEJAR EN BLANCO SI NO TIENE]: ")
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
            while True:
                try:
                    dniPersona = int(input("Ingrese el DNI de la persona a eliminar: "))
                    break
                except ValueError:
                    print("Error: debe ingresar un valor numerico.")
            encontrado = 0
            for persona in listaPersonas:
                if persona.dni == dniPersona:
                    encontrado = 1
                    listaPersonas.remove(persona)
            if encontrado == 0:
                print("No se encontro a la persona indicada. Intente nuevamente. \n")
            continuar()


        case 4:
            while True:
                try:
                    dniPersona = int(input("Ingrese el DNI de la persona a modificar: "))
                    break
                except ValueError:
                    print("Error: debe ingresar un valor numerico.")
            encontrado = 0
            for persona in listaPersonas:
                if persona.dni == dniPersona:
                    encontrado = 1
                    persona.modificarApellidos()
            if encontrado == 0:
                print("No se encontro a la persona indicada. Intente nuevamente.\n")
            continuar()


        case 5:
            while True:
                try:
                    dniPersona = int(input("Ingrese el DNI de la persona a modificar: "))
                    break
                except ValueError:
                    print("Error: debe ingresar un valor numerico.")
            encontrado = 0
            for persona in listaPersonas:
                if persona.dni == dniPersona:
                    encontrado = 1
                    persona.modificarDireccion()
            if encontrado == 0:
                print("No se encontro a la persona indicada. Intente nuevamente. \n")
            continuar()


        case 6:
            while True:
                try:
                    dniPersona = int(input("Ingrese el DNI de la persona a modificar: "))
                    break
                except ValueError:
                    print("Error: debe ingresar un valor numerico.")
            encontrado = 0
            for persona in listaPersonas:
                if persona.dni == dniPersona:
                    encontrado = 1
                    persona.agregarVacuna()
            if encontrado == 0:
                print("No se encontro a la persona indicada. Intente nuevamente. \n")
            continuar()


        case 7:
            while True:
                try:
                    dniPersona = int(input("Ingrese el DNI de la persona a modificar: "))
                    break
                except ValueError:
                    print("Error: debe ingresar un valor numerico.")
            encontrado = 0
            for persona in listaPersonas:
                if persona.dni == dniPersona:
                    encontrado = 1
                    persona.modificarVacuna()
            if encontrado == 0:
                print("No se encontro a la persona indicada. Intente nuevamente. \n")
            continuar()


        case 8:
            while True:
                try:
                    dniPersona = int(input("Ingrese el DNI de la persona a modificar: "))
                    break
                except ValueError:
                    print("Error: debe ingresar un valor numerico.")
            encontrado = 0
            for persona in listaPersonas:
                if persona.dni == dniPersona:
                    encontrado = 1
                    persona.eliminarVacuna()
            if encontrado == 0:
                print("No se encontro a la persona indicada. Intente nuevamente. \n")
            continuar()


        case 9:
            global salir
            salir = 0


if __name__ == "__main__":

    while salir:
        mostrarMenu()
        while True:
            try:
                accion = int(input("Ingrese el numero de accion a realizar: "))
                if accion not in accionesPermitidas:
                    print("Error: no ingreso una accion valida.")
                else:
                    break
            except ValueError:
                print("Error: no ingreso una accion valida.")
            
        ejecutarAccion(accion)
