from persona import Persona

class Personas:
    def __init__(self):
        self.listaPersonas = []


    def ingresarPersona(self):
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
        persona = Persona(dni,nombre1,nombre2,nombre3,nombre4,apellido1,apellido2,apellido3,direccion,telefono)
        self.listaPersonas.append(persona)
        

    def eliminarPersona(self):
        while True:
            try:
                dniPersona = int(input("Ingrese el DNI de la persona a eliminar: "))
                break
            except ValueError:
                print("Error: debe ingresar un valor numerico.")
        encontrado = 0
        for persona in self.listaPersonas:
            if persona.dni == dniPersona:
                encontrado = 1
                self.listaPersonas.remove(persona)
        if encontrado == 0:
            print("No se encontro a la persona indicada. Intente nuevamente. \n")


    def mostrarPersonas(self):
        print("##### LISTA DE PERSONAS #####")
        for i in range(len(self.listaPersonas)):
            print(f"== Persona {i}. == {self.listaPersonas[i]}")


    def modificarPersona(self):
        print("1. Modificar Nombres")
        print("2. Modificar Apellidos")
        print("3. Modificar Direccion")
        print("4. Modificar Telefono")
        print("5. Agregar Vacuna")
        print("6. Modificar Vacunas")
        print("7. Eliminar Vacuna")
        print("8. Salir\n")

        while True:
            try:
                opcion = int(input("Ingrese la accion que desea realizar: "))
                break
            except ValueError:
                print("Error: debe ingresar un valor numerico.")
        
        if opcion == 8:
            return 0

        while True:
            try:
                dniPersona = int(input("Ingrese el DNI de la persona: "))
                break
            except ValueError:
                print("Error: debe ingresar un valor numerico.")

        encontrado = 0
        for persona in self.listaPersonas:
            if persona.dni == dniPersona:
                encontrado = 1
                match opcion:
                    case 1:
                        persona.modificarNombres()
                    case 2:
                        persona.modificarApellidos()
                    case 3:
                        persona.modificarDireccion()
                    case 4:
                        persona.modificarTelefono()
                    case 5:
                        persona.agregarVacuna()
                    case 6:
                        persona.modificarVacuna()
                    case 7:
                        persona.eliminarVacuna()
        if encontrado == 0:
            print("No se encontro a la persona indicada. Intente nuevamente.\n")


