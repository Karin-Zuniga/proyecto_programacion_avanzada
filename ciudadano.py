from comunidad import Comunidad
from enfermedad import Enfermedad
class Ciudadano():
    def __init__(self, id, nombre, comunidad):
        self.__id = id
        self.__nombre_apellido = nombre
        self.__enfermedades = []
        self.__comunidad = comunidad
        self.__contactos = []
        self.__estado = False

    #--------------get--------------------#

    def get_id(self):
        return self.__id
    
    def get_nombre_apellido(self):
        return self.__nombre_apellido
    
    def get_enfermedad(self):
        return self.__enfermedades
    
    def  get_comunidad(self):
        return self.__comunidad
    
    def get_contactos(self):
        return self.__contactos

    def get_estado(self):
        return self.__estado
    #-------------set----------------------#
    
    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id
    
    def set_nombre_apellido(self, nombre_apellido):
        if isinstance(nombre_apellido,str):
            self.__nombre_apellido

    def set_enfermedades(self, enfermedades):
        if isinstance(enfermedades, list):
            self.__enfermedades.append(enfermedades)
   
    def set_comunidad(self, comunidad):
        if isinstance (comunidad, Comunidad):
            self.__comunidad = comunidad

    def set_contactos(self, contactos):
        if isinstance(contactos, list):
            self.__contactos.append(contactos)
    
    def set_estado(self, estado):
        if isinstance (estado, bool):
            self.__estado = estado
