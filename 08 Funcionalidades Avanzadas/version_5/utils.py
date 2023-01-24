from typing import List, Dict

Personas = List[Dict[str, str]]

def format_data_for_display(personas: Personas) -> List[str]:
    lst = []
    for persona in personas:
        lst.append(f'{persona.get("nombre")} {persona.get("apellido")}: {persona.get("cargo")}')
    return lst

def format_data_for_csv(personas: Personas):
    # TODO: implementar el código de la función. 
    raise NotImplementedError()
