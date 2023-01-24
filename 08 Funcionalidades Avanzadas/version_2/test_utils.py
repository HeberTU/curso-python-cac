import pytest
from utils import to_snake_case

def test_dos_palabras():
    assert to_snake_case("hola_mundo") == "hola_mundo"

def test_dos_palabras_mayusculas():
    assert to_snake_case("Curso Python") == "curso_python"
    
def test_una_palabra():
    assert to_snake_case("notebook") == "notebook"

def test_raises_exception_no_string_arg():
    with pytest.raises(TypeError):
        to_snake_case(5)
