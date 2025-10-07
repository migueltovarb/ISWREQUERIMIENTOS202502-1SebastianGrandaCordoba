class Contacto:
    def __init__(self, nombre, apellido, direccion, correo, cargo=""):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.correo = correo
        self.cargo = cargo
        self.telefonos = []

    def darNombre(self):
        return self.nombre

    def darApellido(self):
        return self.apellido

    def darDireccion(self):
        return self.direccion

    def darCorreo(self):
        return self.correo

    def darCargo(self):
        return getattr(self, 'cargo', '')

    def darTelefonos(self):
        if hasattr(self, 'telefonos') and self.telefonos is not None:
            return self.telefonos
        return []

    def cambiarDireccion(self, direccion):
        self.direccion = direccion

    def cambiarCorreo(self, correo):
        self.correo = correo

    def cambiarCargo(self, cargo):
        self.cargo = cargo

    def agregarTelefono(self, telefono):
        if telefono not in self.telefonos:
            self.telefonos.append(telefono)
        else:
            raise ValueError(f"El teléfono {telefono} ya existe en la lista de teléfonos.")

    def eliminarTelefono(self, telefono):
        if telefono in self.telefonos:
            self.telefonos.remove(telefono)
        else:
            raise ValueError(f"El teléfono {telefono} no se encuentra en la lista de teléfonos.")

    def agregarTelefonos(self, telefonos):
        for t in telefonos:
            self.agregarTelefono(t)

    def eliminarTodosLosTelefonos(self):
        self.telefonos.clear()
