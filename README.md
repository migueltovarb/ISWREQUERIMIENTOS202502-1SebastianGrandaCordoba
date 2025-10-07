# ConnectMe - Agenda de Contactos

Este proyecto es una pequeña agenda de contactos para la empresa ConnectMe.

Características relevantes:
-- Cada contacto tiene: nombre, apellido, dirección, correo (identificador único), cargo y teléfonos.
- El correo actúa como identificador único: no se permiten dos contactos con el mismo correo.
- Los contactos se persisten automáticamente en `contactos.csv` en la carpeta del programa (`ListaContactos`) para mantenerlos entre ejecuciones.

Archivos principales:
- `Mundo/Contacto.py` - Clase Contacto.
- `Mundo/ListaDeContactos.py` - Gestión de la lista (búsquedas, agregar, modificar, eliminar, persistencia CSV).
- `main.py` - Interfaz por consola.
- `gui.py` - Interfaz gráfica (tkinter).

Cómo ejecutar

1. Asegúrate de tener Python 3.8+ instalado.
2. Abrir una terminal (PowerShell) en la carpeta `ListaContactos`.

Para ejecutar la interfaz de consola:

```powershell
python main.py
```

Para ejecutar la interfaz gráfica:

```powershell
python gui.py
```

Persistencia

- Al agregar/modificar/eliminar contactos se actualiza `contactos.csv` en la carpeta `ListaContactos`.
- Si `contactos.csv` no existe, se crea al guardar el primer cambio.

Evidencia de funcionamiento

- La suite de tests incluida pasa localmente (pytest) y cubre las operaciones básicas.
- Para comprobar manualmente:
  1. Ejecuta `python main.py`.
  2. Agrega un contacto con correo `test@connectme.local` y cualquier dato.
  3. Cierra el programa.
  4. Abre `contactos.csv` y confirma que existe la fila con `test@connectme.local`.
  5. Ejecuta nuevamente `python main.py` y busca por correo `test@connectme.local` (opción 10) — deberías ver el contacto.


Notas técnicas

-- El campo `telefonos` se guarda en CSV como JSON para preservar listas.
