# test_solucion.py

from solucion import suma_lista

def test_vectores():
    assert suma_lista([1, 2, 3]) == 6
    assert suma_lista([10, -5, 5]) == 10
