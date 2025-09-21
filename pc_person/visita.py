from persona import Persona


class Visita(Persona):
    def __init__(self, dni, nombre1, nombre2, nombre3, nombre4, apellido1, apellido2, apellido3, direccion, telefono, IVacunas, libro, folio, renglon, fechaVisita):
        super().__init__(dni, nombre1, nombre2, nombre3, nombre4, apellido1, apellido2, apellido3, direccion, telefono, IVacunas)
        self.libro = libro
        self.folio = folio
        self.renglon = renglon
        self.fechaVisita = fechaVisita

    def __repr__(self):
        return (f"\nDNI: {self.dni}\n"
                f"NOMBRE/S: {self.nombre1} {self.nombre2} {self.nombre3} {self.nombre4}\n"
                f"APELLIDO/S: {self.apellido1} {self.apellido2} {self.apellido3}\n"
                f"DIRECCION: {self.direccion}\n"
                f"TELEFONO: {self.telefono}\n"
                f"VACUNAS: {self.IVacunas}\n"
                f"LIBRO {self.libro}\n"
                f"FOLIO {self.folio}\n"
                f"RENGLON {self.renglon}\n")

    def modificarFirma(self):
        nuevoLib = input("Ingrese nuevo número de libro: ")
        nuevoFol = input("Ingrese nuevo número de folio: ")
        nuevoRen = input("Ingrese nuevo número de renglon: ")

        self.libro = nuevoLib
        self.folio = nuevoFol
        self.renglon = nuevoRen

    def modificarFechaVisita(self):
        nuevaFec = input("Ingrese fecha de visita modificada: ")
        self.fechaVisita = nuevaFec

