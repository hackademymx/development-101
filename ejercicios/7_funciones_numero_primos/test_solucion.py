# test_solucion.py

from solucion import es_primo

def test_numero_primo():
    assert es_primo(2) == True
    assert es_primo(3) == True
    assert es_primo(13) == True

def test_numero_no_primo():
    assert es_primo(1) == False  # 1 no es primo
    assert es_primo(4) == False
    assert es_primo(9) == False

def test_numeros_especiales():
    assert es_primo(0) == False  # 0 no es primo
    assert es_primo(-5) == False  # Números negativos no son primos