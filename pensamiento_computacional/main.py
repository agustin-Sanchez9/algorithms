import os
from persona import Persona
from personas import Personas



testPerson = Persona(1,"a","b","","","c","d","","as 12",1123)
persona1 = Persona(43906044, "agustin","","","","sanchez","","","lamadrid 85", "1139183587")
persona2 = Persona(43903138,"priscila","belen","","","della vecchia","","","los arces 234","12312313")
listaPersonas = Personas()
listaPersonas.listaPersonas.append(persona1)
listaPersonas.listaPersonas.append(persona2)
listaPersonas.listaPersonas.append(testPerson)
salir = 1
accionesPermitidas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#listaPersonas = [testPerson]


def mostrarMenu():
    print("1. Ingresar persona.")
    print("2. Mostrar personas")
    print("3. Eliminar persona.")
    print("4. Modificar persona.")
    print("5. Salir.\n")


def limpiarTerminal():
    if os.name == 'nt':
        os.system('cls')  # for windows
    else:
        os.system('clear')  # for linux or mac


def continuar():
    respuesta = input("Presione cualquier tecla para continuar... ")
    limpiarTerminal()


def ejecutarAccion(accion):
    match accion:

        case 1:
            listaPersonas.ingresarPersona()
            continuar()

        case 2:
            listaPersonas.mostrarPersonas()
            continuar()

        case 3:
            listaPersonas.eliminarPersona()
            continuar()

        case 4:
            listaPersonas.modificarPersona()
            continuar()

        case 5:
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
