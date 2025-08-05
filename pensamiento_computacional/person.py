

class Persona:
    def __init__(self, dni, nombre, apellido, direccion, telefono):
        if len(nombre.split()) > 4:
            raise ValueError("La persona no puede tener mas de 4 nombres")
        if len(apellido.split()) > 3:
            raise ValueError("La persona no puede tener mas de 3 apellidos")
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono

    def __repr__(self):
        return (f"\nDNI: {self.dni}\n"
                f"NOMBRE: {self.nombre}\n"
                f"APELLIDO: {self.apellido}\n"
                f"DIRECCION: {self.direccion}\n"
                f"TELEFONO: {self.telefono}\n")

    def mostrarPersona(self):
        print(self)

    def mostrarDNI(self):
        print("\nDNI: {dni}\n".format(dni=self.dni))

    def modificarApellido(self):
        nuevoApe = input("Ingrese el apellido modificado: ")
        print("\nEl nuevo apellido es: {apellido}\n".format(apellido=nuevoApe))
        self.apellido = nuevoApe

    def modificarDireccion(self):
        nuevaDir = input("Ingrese la direccion modificada: ")
        self.direccion = nuevaDir


if __name__ == "__main__":

    test = Persona(40000000, "pedro", "paramo a a a", "en la casa", 11123123)

    salir = 1

    while salir:
        print("#########################")
        print("1.Mostrar persona")
        print("2.Mostrar DNI")
        print("3.Modificar apellido")
        print("4.Modificar direccion")
        print("5.Salir")
        print("#########################")

        opcion = input("Ingrese la opcion que desea: ")

        if opcion == "1":
            test.mostrarPersona()
        elif opcion == "2":
            test.mostrarDNI()
        elif opcion == "3":
            test.modificarApellido()
        elif opcion == "4":
            test.modificarDireccion()
        elif opcion == "5":
            salir = 0
