from persona import Persona

class Personal(Persona):
    def __init__(self, dni, nombre1, nombre2, nombre3, nombre4, apellido1, apellido2, apellido3, direccion, telefono, IVacunas, legajo, cargo):
        super().__init__(dni, nombre1, nombre2, nombre3, nombre4, apellido1, apellido2, apellido3, direccion, telefono, IVacunas)
        self.legajo = legajo
        self.cargo = cargo

    def __repr__(self):
        return (f"\nDNI: {self.dni}\n"
                f"NOMBRE/S: {self.nombre1} {self.nombre2} {self.nombre3} {self.nombre4}\n"
                f"APELLIDO/S: {self.apellido1} {self.apellido2} {self.apellido3}\n"
                f"DIRECCION: {self.direccion}\n"
                f"TELEFONO: {self.telefono}\n"
                f"VACUNAS: {self.IVacunas}\n"
                f"LEGAJO: {self.legajo}\n"
                f"CARGO: {self.cargo}\n")


    def modificarLegajo(self):
        nuevoLej = input("Ingrese el nuevo legajo: ")
        self.legajo = nuevoLej

    def modificarCargo(self):
        nuevoCar = input("Ingrese el nuevo cargo: ")
        self.cargo = nuevoCar
