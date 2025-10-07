from Mundo.ListaDeContactos import ListaDeContactos

class Menu:

    def __init__(self):
        self.__miListaDeContactos = ListaDeContactos()
        # Cargar contactos desde CSV (si existe)
        try:
            self.__miListaDeContactos.cargarDesdeCSV()
        except Exception:
            pass

    def MenuPrincipal(self):
        while True:
            print("\n--- LISTA DE CONTACTOS ---")
            print("1. Agregar contacto")
            print("2. Ver todos los contactos")
            # opción de buscar por palabra clave eliminada
            print("4. Buscar por nombre y apellido")
            print("5. Eliminar contacto")
            print("6. Modificar contacto")
            # opciones de favoritos eliminadas
            print("10. Buscar por correo")
            print("0. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                datos = self.SolicitarDatosCompletos()
                # datos = [nombre, apellido, direccion, correo, telefonos, cargo?]
                if len(datos) == 5:
                    nombre, apellido, direccion, correo, telefonos = datos
                    cargo = ""
                else:
                    nombre, apellido, direccion, correo, telefonos, cargo = datos

                agregado = self.__miListaDeContactos.agregarContacto(nombre, apellido, direccion, correo, telefonos)
                if agregado:
                    try:
                        self.__miListaDeContactos.guardarEnCSV()
                    except Exception:
                        pass
                    print("\n✅ Contacto agregado.")
                else:
                    print("\n❌ No se pudo agregar el contacto.")

            elif opcion == "2":
                contactos = self.__miListaDeContactos.darTodosLosContactos()
                if not contactos:
                    print("\n📭 No hay contactos.")
                else:
                    for c in contactos:
                        self.MostrarContacto(c)

            # buscar por palabra clave eliminada

            elif opcion == "4":
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                contacto = self.__miListaDeContactos.buscarContacto(nombre, apellido)
                if contacto:
                    self.MostrarContacto(contacto)
                else:
                    print(f"\n❌ Contacto {nombre} {apellido} no encontrado.")

            elif opcion == "5":
                nombre = input("Nombre a eliminar: ")
                apellido = input("Apellido: ")
                contacto = self.__miListaDeContactos.buscarContacto(nombre, apellido)
                if not contacto:
                    print("\n❌ Contacto no encontrado.")
                else:
                    confirmar = input(f"¿Confirma eliminar a {nombre} {apellido}? (s/n): ").strip().lower()
                    if confirmar == 's':
                        if self.__miListaDeContactos.eliminarContacto(nombre, apellido):
                            try:
                                self.__miListaDeContactos.guardarEnCSV()
                            except Exception:
                                pass
                            print("\n✅ Contacto eliminado.")
                        else:
                            print("\n❌ No se pudo eliminar el contacto.")
                    else:
                        print("\n⚠️ Operación cancelada.")

            elif opcion == "6":
                self.ModificarContacto()

            # opciones de favoritos eliminadas

            elif opcion == "10":
                correo = input("Correo: ")
                contacto = self.__miListaDeContactos.buscarContactoPorCorreo(correo)
                if contacto:
                    self.MostrarContacto(contacto)
                else:
                    print(f"\n❌ No existe un contacto con el correo {correo}.")

            elif opcion == "0":
                print("\n👋 Adiós.")
                break

            else:
                print("\n❌ Opción inválida.")

    def MostrarContacto(self, contacto):
        try:
            print("\n------------------------")
            print(f"Nombre: {contacto.darNombre()} {contacto.darApellido()}")
            print(f"Dirección: {contacto.darDireccion()}")
            print(f"Cargo: {contacto.darCargo()}")
            print(f"Correo: {contacto.darCorreo()}")
            print("Teléfonos:", ", ".join(contacto.darTelefonos()))
            # Palabras clave eliminadas
            print("------------------------")
        except Exception as e:
            print("❌ Error mostrando contacto:", e)

    def SolicitarDatosCompletos(self):
        nombre = input("Digite nombre: ")
        apellido = input("Digite apellido: ")
        direccion = input("Digite dirección: ")
        correo = input("Digite correo: ")
        cargo = input("Digite cargo (empresa ConnectMe): ")
        telefonos = self.AgregarTelefonos()
        return [nombre, apellido, direccion, correo, telefonos, cargo]

    def AgregarTelefonos(self):
        telefonos = []
        while True:
            telefono = input("Digite teléfono: ")
            if telefono.isdigit():
                telefonos.append(telefono)
            else:
                print("❌ No es un número válido.")
            op = input("¿Agregar otro teléfono? (s/n): ").lower()
            if op != 's':
                break
        return telefonos

    def AgregarPalabras(self, nombre, apellido):
        # Método eliminado: ya no se solicitan palabras clave en la aplicación
        return []

    def ModificarContacto(self):
        nombre = input("Nombre del contacto a modificar: ")
        apellido = input("Apellido: ")
        contacto = self.__miListaDeContactos.buscarContacto(nombre, apellido)
        if not contacto:
            print("❌ Contacto no encontrado.")
            return

        print("Ingrese nuevos datos:")
        direccion = input("Nueva dirección: ")
        correo = input("Nuevo correo: ")
        cargo = input("Nuevo cargo (empresa ConnectMe): ")
        telefonos = self.AgregarTelefonos()
        modified = self.__miListaDeContactos.modificarContacto(nombre, apellido, direccion, correo, telefonos)
        if modified:
            contacto.cambiarCargo(cargo)
            try:
                self.__miListaDeContactos.guardarEnCSV()
            except Exception:
                pass
            print("✅ Contacto modificado.")
        else:
            print("\n❌ No se pudo modificar el contacto (correo duplicado?).")

if __name__ == "__main__":
    menu = Menu()
    menu.MenuPrincipal()
