# test_solucion.py

from solucion import convertir_a_mayusculas

def test_strings():
    assert convertir_a_mayusculas("hola") == "HOLA"
    assert convertir_a_mayusculas("Python") == "PYTHON"
