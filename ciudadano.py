from comunidad import Comunidad
from enfermedad import Enfermedad
import numpy as np
class Ciudadano():
    def __init__(self, id, nombre, comunidad):
        self.__id = id
        self.__nombre_apellido = nombre
        self.__enfermedades = []
        self.__comunidad = comunidad
        self.__contactos = []
        self.__estado = 1
        #self.estado: 1=sano 2=enfermo 3=recuperado/muerto

    #--------------get--------------------#

    def get_id(self):
        return self.__id
    
    def get_nombre_apellido(self):
        return self.__nombre_apellido
    
    def get_enfermedad(self):
        return self.__enfermedades
    
    def  get_comunidad(self):
        return self.__comunidad.get_nombre()
    
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
        if isinstance(enfermedades,Enfermedad):
            self.__enfermedades.append(enfermedades)
        else:
            print("error al agregar")
   
    def set_comunidad(self, comunidad):
        if isinstance (comunidad, Comunidad):
            self.__comunidad = comunidad

    def set_contactos(self, contactos):
        if isinstance(contactos, Ciudadano):
            self.__contactos.append(contactos)
            
    
    def set_estado(self, estado):
        self.__estado = estado

    


