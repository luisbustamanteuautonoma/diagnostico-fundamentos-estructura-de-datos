from persona import Persona
class Profesional(Persona):
    def __init__(self, nombre, edad, sexo, profesion, sueldo):
        super().__init__(nombre, edad, sexo)
        self.__profesion = profesion
        self.__sueldo = sueldo
    
    def get_profesion(self):
        return self.__profesion
    def set_profesion(self, profesion):
        self.__profesion = profesion
    
    def get_sueldo(self):
        return self.__sueldo
    def set_sueldo(self, sueldo):
        self.__sueldo = sueldo
