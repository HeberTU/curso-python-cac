def to_snake_case(x: str) -> str:
    return '_'.join(x.lower().split())