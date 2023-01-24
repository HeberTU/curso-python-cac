def to_snake_case(x: str) -> str:
    if not isinstance(x, str):
        raise TypeError('El argumento x debe ser un string')
    return '_'.join(x.lower().split())