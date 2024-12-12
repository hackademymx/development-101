# test_solucion.py

from solucion import edad, nombre, presentar

def test_tipos_correctos():
    assert isinstance(edad, int), "La variable `edad` debe ser un entero"
    assert isinstance(nombre, str), "La variable `nombre` debe ser un string"

def test_valores_correctos():
    assert edad == 25, "La variable `edad` debe ser igual a 25"
    assert "Mi nombre es" in presentar(), "El formato del mensaje es incorrecto"
