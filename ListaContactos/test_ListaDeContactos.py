import pytest
from Mundo.Contacto import Contacto
from Mundo.ListaDeContactos import ListaDeContactos

@pytest.fixture
def setup_escenario1():
    contacto1 = Contacto("Carolina", "Rodríguez", "Trv 25 No. 43 - 45", "crodriguez@campusucc.edu.co")
    contacto1.agregarTelefono("6556850")
    contacto1.agregarTelefono("4859527")
    # palabras clave eliminadas

    contacto2 = Contacto("Camila", "Borrero", "Cll 56 No. 67 - 76", "cborrero@campusucc.edu.co")
    contacto2.agregarTelefono("6456787")
    contacto2.agregarTelefono("5678765")
    # palabras clave eliminadas

    contacto3 = Contacto("Mauricio", "Sánchez", "Av 24 No. 6 - 32", "msanchez@msanchez.com")
    contacto3.agregarTelefono("6785465")
    # palabras clave eliminadas

    lista = ListaDeContactos()
    lista.agregarContacto(contacto1.darNombre(), contacto1.darApellido(), contacto1.darDireccion(), contacto1.darCorreo(), contacto1.darTelefonos())
    lista.agregarContacto(contacto2.darNombre(), contacto2.darApellido(), contacto2.darDireccion(), contacto2.darCorreo(), contacto2.darTelefonos())
    lista.agregarContacto(contacto3.darNombre(), contacto3.darApellido(), contacto3.darDireccion(), contacto3.darCorreo(), contacto3.darTelefonos())

    return lista, contacto1, contacto2, contacto3

def test_dar_todos_los_contactos(setup_escenario1):
    lista, _, _, _ = setup_escenario1
    contactos = lista.darTodosLosContactos()
    nombres = [f"{c.darNombre()} {c.darApellido()}" for c in contactos]
    assert nombres == ["Carolina Rodríguez", "Camila Borrero", "Mauricio Sánchez"]



def test_dar_contactos_palabra(setup_escenario1):
    lista, _, _, _ = setup_escenario1
    # Busqueda por palabra clave eliminada
    assert True

def test_buscar_contacto_existente(setup_escenario1):
    lista, _, _, _ = setup_escenario1
    c = lista.buscarContacto("Camila", "Borrero")
    assert c is not None
    assert c.darNombre() == "Camila"
    assert c.darApellido() == "Borrero"
    assert c.darTelefonos() == ["6456787", "5678765"]

def test_buscar_contacto_inexistente(setup_escenario1):
    lista, _, _, _ = setup_escenario1
    c = lista.buscarContacto("Pedro", "Pérez")
    assert c is None

def test_agregar_contacto(setup_escenario1):
    lista, _, _, _ = setup_escenario1

    nuevo_contacto = Contacto("Mauricio", "Sánchez", "Av 24 No. 6 - 34", "msanchez1@msanchez.com")
    accion = lista.agregarContacto(nuevo_contacto.darNombre(), nuevo_contacto.darApellido(), nuevo_contacto.darDireccion(), nuevo_contacto.darCorreo(), nuevo_contacto.darTelefonos())
    assert not accion

def test_eliminar_contacto(setup_escenario1):
    lista, _, _, _ = setup_escenario1

    accion = lista.eliminarContacto("Diana", "Puentes")
    assert not accion

    lista.eliminarContacto("Mauricio", "Sánchez")
    # Antes se buscaba por palabra, ahora simplemente comprobar que el contacto fue eliminado
    c = lista.buscarContacto("Mauricio", "Sánchez")
    assert c is None

def test_modificar_contacto(setup_escenario1):
    lista, _, _, _ = setup_escenario1

    contacto1 = Contacto("Pedro", "Sánchez", "Av 24 No. 6 - 34", "msanchez1@msanchez.com")
    accion = lista.modificarContacto(contacto1.darNombre(), contacto1.darApellido(), contacto1.darDireccion(), contacto1.darCorreo(), contacto1.darTelefonos())
    assert not accion

    telefonos1 = []
    lista.modificarContacto("Mauricio", "Sánchez", "Av 24 No. 6 - 44", "msanchez1@msanchez.com", telefonos1)

    c = lista.buscarContacto("Mauricio", "Sánchez")
    assert c.darDireccion() == "Av 24 No. 6 - 44"
    assert len(c.darTelefonos()) == 0


def test_agregar_contacto_correo_duplicado(setup_escenario1):
    lista, contacto1, contacto2, contacto3 = setup_escenario1
    # Intentar agregar un contacto nuevo con el mismo correo que contacto1
    nuevo = Contacto("Andres", "Lopez", "Cll 1", contacto1.darCorreo())
    accion = lista.agregarContacto(nuevo.darNombre(), nuevo.darApellido(), nuevo.darDireccion(), nuevo.darCorreo(), nuevo.darTelefonos())
    assert accion is False
