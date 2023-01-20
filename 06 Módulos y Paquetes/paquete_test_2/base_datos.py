class Conexion():
    def __init__(self, url: str):
            self.url = url
         
    

class BaseDatos():
    def __init__(self, conexion: Conexion):
            self.conexion = conexion
