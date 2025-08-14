
class Persona:
    def __init__(self, dni, nombre1, nombre2, nombre3, nombre4, apellido1, apellido2, apellido3, direccion, telefono):
        self.dni = dni
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.nombre3 = nombre3
        self.nombre4 = nombre4
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.apellido3 = apellido3
        self.direccion = direccion
        self.telefono = telefono
        self.IVacunas = []

    def __repr__(self):
        return (f"\nDNI: {self.dni}\n"
                f"NOMBRE/S: {self.nombre1} {self.nombre2} {self.nombre3} {self.nombre4}\n"
                f"APELLIDO/S: {self.apellido1} {self.apellido2} {self.apellido3}\n"
                f"DIRECCION: {self.direccion}\n"
                f"TELEFONO: {self.telefono}\n"
                f"VACUNAS: {self.IVacunas}")


    def mostrarPersona(self):
        print(self)


    def mostrarDNI(self):
        print("\nDNI: {dni}\n".format(dni=self.dni))


    def modificarApellidos(self):
        print("Que apellido desea modificar?")
        print(f"1. PRIMER APELLIDO: {self.apellido1}")
        print(f"2. SEGUN APELLIDO: {self.apellido2}")
        print(f"3. TERCER AEPLLIDO: {self.apellido3}")
        option = int(input("Ingrese el numero correspondiente: "))
        while option not in [1, 2, 3]:
            print("ERROR: El valor ingresado no es valido.")
            option = int(input("Intente nuevamente: "))
        nuevoApe = input("\nIngrese el apellido modificado: ")
        match option:
            case 1:
                self.apellido1 = nuevoApe
            case 2:
                self.apellido2 = nuevoApe
            case 3:
                self.apellido3 = nuevoApe
        print(f"\nEl nuevo apellido es: {nuevoApe}")


    def modificarDireccion(self):
        nuevaDir = input("Ingrese la direccion modificada: ")
        self.direccion = nuevaDir


    def agregarVacuna(self):
        nuevaVacuna = input("Ingrese la vacuna a agregar: ")
        self.IVacunas.append(nuevaVacuna)


    def modificarVacuna(self):
        for idx, vacuna in enumerate(self.IVacunas):
            print(f"{idx}. {vacuna}.")
        while True:
            try:
                nroVacuna = int(input("Ingrese el numero de la vacuna a eliminar: "))
                if nroVacuna > len(self.IVacunas) or nroVacuna < 0:
                    print("ERROR: Valor de la vacuna no es valido")
                else:
                    break
            except ValueError:
                print("ERROR: Valor de la vacuna no es valido")
        print(f"\nUsted selecciono la vacuna: {nroVacuna}. {self.IVacunas[nroVacuna]}.\n")
        nuevaVacuna = input("Ingrese la modificacion: ")
        self.IVacunas[nroVacuna] = nuevaVacuna


    def eliminarVacuna(self):
        for idx, vacuna in enumerate(self.IVacunas):
            print(f"{idx}. {vacuna}.")
        while True:
            try:
                nroVacuna = int(input("Ingrese el numero de la vacuna a eliminar: "))
                if nroVacuna > len(self.IVacunas) or nroVacuna < 0:
                    print("ERROR: Valor de la vacuna no es valido")
                else:
                    break
            except ValueError:
                print("ERROR: Valor de la vacuna no es valido")
        print(f"\nUsted selecciono la vacuna: {nroVacuna}. {self.IVacunas[nroVacuna]}.\n")
        del self.IVacunas[nroVacuna]
