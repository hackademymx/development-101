# test_solucion.py

from solucion import Persona

def test_poo():
    persona = Persona("Juan", 30)
    assert persona.nombre == "Juan"
    assert persona.edad == 30
    assert persona.saludar() == "Hola, mi nombre es Juan y tengo 30 años"
