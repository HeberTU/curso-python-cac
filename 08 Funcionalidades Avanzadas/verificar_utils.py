from utils import to_snake_case

def verificar_utils():
    
    print(to_snake_case("hola mundo") == "hola_mundo")
    print(to_snake_case("Curso Python") == "curso_python")
    print(to_snake_case("notebook") == "notebook")
    
if __name__ == '__main__':
    verificar_utils()