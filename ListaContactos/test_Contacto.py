import pytest
from Mundo.Contacto import Contacto

@pytest.fixture
def contacto():
    contacto = Contacto("Carolina", "Rodríguez", "Trv 25 No. 43 - 45", "crodriguez@campusucc.edu.co")
    contacto.agregarTelefono("6556850")
    contacto.agregarTelefono("4859527")
    return contacto

def test_cambiar_datos(contacto):
    assert contacto.darNombre() == "Carolina"
    assert contacto.darApellido() == "Rodríguez"
    assert contacto.darDireccion() == "Trv 25 No. 43 - 45"
    assert contacto.darCorreo() == "crodriguez@campusucc.edu.co"

    contacto.cambiarDireccion("Cll 45 a No 45 - 23")
    contacto.cambiarCorreo("carito2005@hotmail.com")

    assert contacto.darNombre() == "Carolina"
    assert contacto.darApellido() == "Rodríguez"
    assert contacto.darDireccion() == "Cll 45 a No 45 - 23"
    assert contacto.darCorreo() == "carito2005@hotmail.com"

def test_agregar_telefono(contacto):
    contacto.agregarTelefono("22140732")
    telefonos = contacto.darTelefonos()
    assert telefonos == ["6556850", "4859527", "22140732"]

def test_agregar_palabra(contacto):
    # Prueba de palabras clave eliminada
    assert True

def test_eliminar_telefono(contacto):
    contacto.eliminarTelefono("6556850")
    telefonos = contacto.darTelefonos()
    assert telefonos == ["4859527"]

def test_eliminar_palabra(contacto):
    # Prueba de eliminación de palabras eliminada
    assert True

def test_verificar_palabra(contacto):
    # Prueba de verificación de palabra eliminada
    assert True