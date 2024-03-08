
class Persona:
    def __init__(self, nombre, edad, sexo):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_edad(self):
        return self.__edad
    def set_edad(self, edad):
        self.__edad = edad

    def get_sexo(self):
        return self.__sexo
    def set_sexo(self, sexo):
        self.__sexo = sexo
