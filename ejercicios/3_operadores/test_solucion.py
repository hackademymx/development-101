# test_solucion.py

from solucion import sumar, restar, residuo

def test_operadores():
    assert sumar(10, 5) == 15
    assert restar(10, 5) == 5
    assert residuo(10, 3) == 1
