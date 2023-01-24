import pytest
from utils import Personas

@pytest.fixture
def personas() -> Personas:
    return [
        {
            "nombre": "Heber",
            "apellido": "Trujillo",
            "cargo": "Machine Learning Enineer",
        },
        {
            "nombre": "Montserrat",
            "apellido": "Navarro",
            "cargo": "Data Enineer",
        },
    ]