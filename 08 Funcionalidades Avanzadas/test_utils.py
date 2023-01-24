import pytest
from utils import to_snake_case

def test_dos_palabras():
    assert to_snake_case(2) == "hola_mundo"

def test_dos_palabras_mayusculas():
    assert to_snake_case("Curso Python") == "curso_python"
    
def test_una_palabra():
    assert to_snake_case("notebook") == "notebook"