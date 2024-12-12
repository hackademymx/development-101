# test_solucion.py

from solucion import par_impar

def test_estructuras_control():
    assert par_impar(4) == "Par"
    assert par_impar(7) == "Impar"
