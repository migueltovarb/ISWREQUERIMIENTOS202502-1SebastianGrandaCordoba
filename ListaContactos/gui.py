import tkinter as tk
from tkinter import messagebox, simpledialog
from Mundo.ListaDeContactos import ListaDeContactos

class ContactosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ConnectMe")
        self.lista = ListaDeContactos()
        # Cargar contactos desde CSV si existe
        try:
            self.lista.cargarDesdeCSV()
        except Exception:
            pass

        tk.Button(root, text="Agregar Contacto", width=25, command=self.agregar_contacto).pack(pady=5)
        tk.Button(root, text="Ver Todos los Contactos", width=25, command=self.ver_contactos).pack(pady=5)
        tk.Button(root, text="Buscar Contacto por Nombre", width=25, command=self.buscar_contacto).pack(pady=5)
        tk.Button(root, text="Buscar Contacto por Correo", width=25, command=self.buscar_por_correo).pack(pady=5)
        tk.Button(root, text="Modificar Contacto", width=25, command=self.modificar_contacto).pack(pady=5)
        tk.Button(root, text="Eliminar Contacto", width=25, command=self.eliminar_contacto).pack(pady=5)
    # Botones de palabras clave y favoritos eliminados
        tk.Button(root, text="Salir", width=25, command=root.quit).pack(pady=10)

    def agregar_contacto(self):
        ventana = self.crear_formulario_contacto("Agregar Contacto")
        if ventana:
            nombre, apellido, direccion, correo, telefonos, cargo = ventana
            ok = self.lista.agregarContacto(nombre, apellido, direccion, correo, telefonos, cargo)
            if ok:
                try:
                    self.lista.guardarEnCSV()
                except Exception:
                    pass
                messagebox.showinfo("Éxito", "Contacto agregado correctamente")
            else:
                messagebox.showerror("Error", "No se pudo agregar el contacto. Puede que ya exista el nombre/apellido o el correo esté en uso.")

    def ver_contactos(self):
        self.mostrar_lista_contactos(self.lista.darTodosLosContactos(), "Todos los Contactos")

    def buscar_por_palabra(self):
        # Buscar por palabra clave eliminado
        messagebox.showinfo("Info", "La búsqueda por palabra clave fue eliminada.")

    def buscar_contacto(self):
        nombre = simpledialog.askstring("Buscar", "Ingrese nombre:")
        apellido = simpledialog.askstring("Buscar", "Ingrese apellido:")
        c = self.lista.buscarContacto(nombre, apellido)
        if c:
            self.mostrar_detalle_contacto(c)
        else:
            messagebox.showerror("Error", "Contacto no encontrado.")

    def modificar_contacto(self):
        nombre = simpledialog.askstring("Modificar", "Nombre del contacto a modificar:")
        apellido = simpledialog.askstring("Modificar", "Apellido:")
        c = self.lista.buscarContacto(nombre, apellido)
        if not c:
            messagebox.showerror("Error", "Contacto no encontrado.")
            return
        ventana = self.crear_formulario_contacto("Modificar Contacto", c)
        if ventana:
            # ventana -> [nombre, apellido, direccion, correo, telefonos(list), cargo]
            nueva_dir = ventana[2]
            nuevo_correo = ventana[3]
            nuevos_tel = ventana[4]
            nuevo_cargo = ventana[5] if len(ventana) > 5 else ""

            modified = self.lista.modificarContacto(nombre, apellido, nueva_dir, nuevo_correo, nuevos_tel)
            if modified:
                # actualizar cargo en el objeto existente
                c.cambiarCargo(nuevo_cargo)
                try:
                    self.lista.guardarEnCSV()
                except Exception:
                    pass
                messagebox.showinfo("Éxito", "Contacto modificado correctamente")
            else:
                messagebox.showerror("Error", "No se pudo modificar el contacto (correo duplicado?).")

    def eliminar_contacto(self):
        nombre = simpledialog.askstring("Eliminar", "Nombre:")
        apellido = simpledialog.askstring("Eliminar", "Apellido:")
        if self.lista.eliminarContacto(nombre, apellido):
            messagebox.showinfo("Éxito", "Contacto eliminado.")
        else:
            messagebox.showerror("Error", "Contacto no encontrado.")

    def ver_favoritos(self):
        messagebox.showinfo("Info", "La funcionalidad de favoritos fue eliminada.")

    def agregar_favorito(self):
        messagebox.showinfo("Info", "La funcionalidad de favoritos fue eliminada.")

    def eliminar_favorito(self):
        messagebox.showinfo("Info", "La funcionalidad de favoritos fue eliminada.")

    def crear_formulario_contacto(self, titulo, contacto=None):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)

        labels = ["Nombre", "Apellido", "Dirección", "Correo", "Teléfonos (coma)", "Cargo"]
        entradas = []

        valores_iniciales = [
            contacto.darNombre() if contacto else "",
            contacto.darApellido() if contacto else "",
            contacto.darDireccion() if contacto else "",
            contacto.darCorreo() if contacto else "",
            ", ".join(contacto.darTelefonos()) if contacto else "",
            contacto.darCargo() if contacto else ""
        ]

        for i, label in enumerate(labels):
            tk.Label(ventana, text=label).grid(row=i, column=0)
            entry = tk.Entry(ventana, width=40)
            entry.insert(0, valores_iniciales[i])
            entry.grid(row=i, column=1)
            entradas.append(entry)

        resultado = []

        def confirmar():
            nonlocal resultado
            resultado = [e.get().strip() for e in entradas]
            if not all(resultado[:4]):
                messagebox.showerror("Error", "Nombre, apellido, dirección y correo son obligatorios.")
                return
            # convertir el campo de teléfonos (índice 4) a lista
            telefonos_raw = resultado[4]
            telefonos = [t.strip() for t in telefonos_raw.split(",") if t.strip()]
            cargo = resultado[5] if len(resultado) > 5 else ""
            # Validar unicidad de correo
            correo = resultado[3]
            existente = self.lista.buscarContactoPorCorreo(correo)
            if contacto is None:
                # Al crear nuevo contacto, no debe existir ya el correo
                if existente is not None:
                    messagebox.showerror("Error", "El correo ya está en uso por otro contacto.")
                    return
            else:
                # Al modificar, permitir el mismo correo del contacto actual, pero no otro contacto
                if existente is not None and existente is not contacto:
                    messagebox.showerror("Error", "El correo ya está en uso por otro contacto.")
                    return

            resultado = [resultado[0], resultado[1], resultado[2], resultado[3], telefonos, cargo]
            ventana.destroy()

        tk.Button(ventana, text="Guardar", command=confirmar).grid(row=len(labels), columnspan=2)
        ventana.wait_window()
        return resultado if resultado else None

    def mostrar_lista_contactos(self, lista, titulo):
        ventana = tk.Toplevel(self.root)
        ventana.title(titulo)
        if not lista:
            tk.Label(ventana, text="No hay contactos.").pack()
        for c in lista:
            texto = f"{c.darNombre()} {c.darApellido()} | {c.darCargo()} | {c.darCorreo()} | Tel: {', '.join(c.darTelefonos())}"
            tk.Label(ventana, text=texto).pack(anchor='w')

    def mostrar_detalle_contacto(self, c):
        detalle = (
            f"Nombre: {c.darNombre()}\n"
            f"Apellido: {c.darApellido()}\n"
            f"Dirección: {c.darDireccion()}\n"
            f"Cargo: {c.darCargo()}\n"
            f"Correo: {c.darCorreo()}\n"
            f"Teléfonos: {', '.join(c.darTelefonos())}"
        )
        messagebox.showinfo("Detalle del contacto", detalle)

    def buscar_por_correo(self):
        correo = simpledialog.askstring("Buscar por correo", "Ingrese correo:")
        if correo:
            c = self.lista.buscarContactoPorCorreo(correo)
            if c:
                self.mostrar_detalle_contacto(c)
            else:
                messagebox.showerror("Error", "Contacto no encontrado.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactosApp(root)
    root.mainloop()
