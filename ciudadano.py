from comunidad import Comunidad
from enfermedad import Enfermedad
class Ciudadano():
    def __init__(self, comunidad):
        self.__id = id
        self.__nombre_apellido = ""
        self.__enfermedades = []
        self.__comunidad = comunidad

    #--------------get--------------------#

    def get_id(self):
        return self.__id
    
    def get_nombre_apellido(self):
        return self.__nombre_apellido
    
    def get_enfermedad(self):
        return self.__enfermedades
    
    def  get_comunidad(self):
        return self.__comunidad
    
    #-------------set----------------------#
    
    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id
    
    def set_nombre_apellido(self, nombre_apellido):
        if isinstance(nombre_apellido,str):
            self.__nombre_apellido

    def add_enfermedades(self, enfermedades):
        if isinstance(enfermedades,Enfermedad):
            self.__enfermedades.append(enfermedades)

    def set_comunidad(self, comunidad):
        if isinstance (comunidad, Comunidad):
            self.__comunidad = comunidad