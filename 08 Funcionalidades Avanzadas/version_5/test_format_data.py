import pytest
from utils import format_data_for_display, format_data_for_csv, Personas

@pytest.mark.unit
def test_format_data_for_display(personas: Personas):

    assert format_data_for_display(personas) == [
        "Heber Trujillo: Machine Learning Enineer",
        "Montserrat Navarro: Data Enineer",
    ]

@pytest.mark.e2e
def test_format_data_for_csv(personas: Personas):
    assert format_data_for_csv(personas) == "nombre,apellido,cargo\nHeber,Trujillo,Machine Learning Enineer\nMontserrat,Navarro,Data Enineer"
