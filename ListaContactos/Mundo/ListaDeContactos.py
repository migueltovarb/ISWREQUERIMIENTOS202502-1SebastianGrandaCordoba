

# Importación de la clase Contacto
from Mundo.Contacto import Contacto
import csv
import json
from pathlib import Path
import os

# Definición de la clase ListaDeContactos
class ListaDeContactos:

    # Atributos de la clase ListaDeContactos

    # Iniciador
    __Method__ = "iniciador"
    __Descri__ = "Inicializa la lista de contactos"
    __Entrys__ = []
    __Return__ = "Lista de contactos vacía"

    def __init__(self):
        self.contactos = []
        self.telefonos = []
        # Ruta del archivo CSV en la carpeta del programa (carpeta ListaContactos)
        self._csv_path = Path(__file__).resolve().parents[1] / 'contactos.csv'

    # Métodos Funcionales

    __Method__ = "darTodosLosContactos"
    __Descri__ = "Devuelve la lista de todos los contactos"
    __Entrys__ = []
    __Return__ = "lista de contactos"

    def darTodosLosContactos(self):
        return self.contactos
    
    # búsqueda por palabra clave eliminada
    
    __Method__ = "buscarContacto"
    __Descri__ = "Busca un contacto por nombre y apellido"
    __Entrys__ = ["nombre", "apellido"]
    __Return__ = "contacto encontrado o None si no existe"

    def buscarContacto(self, nombre, apellido):
        for contacto in self.contactos:
            if contacto.darNombre() == nombre and contacto.darApellido() == apellido:
                return contacto
        return None

    __Method__ = "buscarContactoPorCorreo"
    __Descri__ = "Busca un contacto por correo electr\u00f3nico"
    __Entrys__ = ["correo"]
    __Return__ = "contacto encontrado o None si no existe"

    def buscarContactoPorCorreo(self, correo):
        for contacto in self.contactos:
            if contacto.darCorreo() == correo:
                return contacto
        return None

    def _load_from_csv(self):
        # Si no existe el archivo, no hacer nada
        if not self._csv_path.exists():
            return

        with self._csv_path.open(newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.contactos = []
            for row in reader:
                nombre = row.get('nombre', '')
                apellido = row.get('apellido', '')
                direccion = row.get('direccion', '')
                correo = row.get('correo', '')
                cargo = row.get('cargo', '')
                # telefonos se almacenan como JSON
                try:
                    telefonos = json.loads(row.get('telefonos', '[]'))
                except Exception:
                    telefonos = [t for t in row.get('telefonos', '').split(';') if t]
                c = Contacto(nombre, apellido, direccion, correo, cargo)
                c.agregarTelefonos(telefonos)
                self.contactos.append(c)

    def cargarDesdeCSV(self):
        try:
            self._load_from_csv()
        except Exception:
            pass

    def guardarEnCSV(self):
        try:
            self._save_to_csv()
        except Exception:
            pass

    def _save_to_csv(self):
        # Asegurar carpeta
        csv_path = self._csv_path
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        fieldnames = ['nombre', 'apellido', 'direccion', 'correo', 'cargo', 'telefonos']
        with csv_path.open('w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for c in self.contactos:
                row = {
                    'nombre': c.darNombre(),
                    'apellido': c.darApellido(),
                    'direccion': c.darDireccion(),
                    'correo': c.darCorreo(),
                    'cargo': getattr(c, 'cargo', ''),
                    'telefonos': json.dumps(c.darTelefonos(), ensure_ascii=False)
                }
                writer.writerow(row)
    
    __Method__ = "agregarContacto"
    __Descri__ = "Agrega un nuevo contacto a la lista"
    __Entrys__ = ["nombre", "apellido", "direccion", "correo", "telefonos"]
    __Return__ = "nada"

    def agregarContacto(self, nombre, apellido, direccion, correo, telefonos, cargo=""):
        # Verifica si ya existe un contacto con el mismo nombre y apellido
        if self.buscarContacto(nombre, apellido):
            return False

        # Verifica unicidad de correo
        for c in self.contactos:
            if c.darCorreo() == correo:
                return False

        # Crear el contacto; mantener compatibilidad con constructor que ahora acepta cargo opcional
        nuevoContacto = Contacto(nombre, apellido, direccion, correo, cargo)
        nuevoContacto.agregarTelefonos(telefonos)
        self.contactos.append(nuevoContacto)
        return True


    __Method__ = "eliminarContacto"
    __Descri__ = "Elimina un contacto de la lista por nombre y apellido"
    __Entrys__ = ["nombre", "apellido"]
    __Return__ = "nada"

    def eliminarContacto(self, nombre, apellido):
        assert isinstance(nombre, str) and isinstance(apellido, str), "Nombre y apellido deben ser cadenas de texto"
        contacto = self.buscarContacto(nombre, apellido)
        if contacto:
            self.contactos.remove(contacto)
            return True
        else:
            return False

    __Method__ = "modificarContacto"
    __Descri__ = "Modifica los datos de un contacto existente"
    __Entrys__ = ["nombre", "apellido", "direccion", "correo", "telefonos"]
    __Return__ = "nada"

    def modificarContacto(self, nombre, apellido, direccion, correo, telefonos):
        assert isinstance(nombre, str) and isinstance(apellido, str), "Nombre y apellido deben ser cadenas de texto"
        contacto = self.buscarContacto(nombre, apellido)
        if contacto:
            # Si el correo cambia, verificar que no pertenezca a otro contacto
            if correo != contacto.darCorreo():
                for c in self.contactos:
                    if c is not contacto and c.darCorreo() == correo:
                        return False

            contacto.cambiarDireccion(direccion)
            contacto.cambiarCorreo(correo)
            self.actualizarTelefonos(telefonos, contacto)
            return True
        return False

    __Method__ = "actualizarTelefonos"
    __Descri__ = "Actualiza la lista de teléfonos de un contacto"
    __Entrys__ = ["telefonos", "contacto"]
    __Return__ = "nada"

    def actualizarTelefonos(self, telefonos, contacto):
        # Elimina todos los teléfonos actuales del contacto
        contacto.eliminarTodosLosTelefonos()
        # Agrega los nuevos teléfonos
        contacto.agregarTelefonos(telefonos)

    # actualizarPalabras eliminada (ya no se manejan palabras clave)

    # Metodos Adicionales

    __Method__ = "TotalContactos"
    __Descri__ = "Devuelve el número total de contactos en la lista"
    __Entrys__ = []
    __Return__ = "Retorna el numero total de contactos"

    def TotalContactos(self):
        return len(self.contactos)
    
    # Favoritos eliminados